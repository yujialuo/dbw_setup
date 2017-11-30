#!/usr/bin/env python

import rospy
import av, cv2
import Queue, thread
import numpy as np
#from PIL import Image
from sensor_msgs.msg import Image, CompressedImage, CameraInfo
from cv_bridge import CvBridge

import config

class Compressor():

    def __init__(self, mode, image_is_compressed):
        self.mode = mode
        self.image_is_compressed = image_is_compressed
        self.img_queue = Queue.Queue()
        self.time_queue = Queue.Queue()

        self.is_recording = False
        self.is_running = True

        self.buffer_size = config.max_frames
        self.frame_count = 0
        self.video_count = 0

        self.rc_method = config.rc_method.split(' ')
        
        self.container = None
        self.stream    = None
        self.log       = None 
        self.frame_count = 0
        self.received_count = 0

	self.bridge = CvBridge()

        thread.start_new_thread(self.compressing,())

    def __del__(self):
        self.is_running = False

    def addNewFrame(self, stamp):
        if not self.container or not self.stream:
            return

        data = self.img_queue.get()

        if self.image_is_compressed:
            np_arr = np.fromstring(data.data, np.uint8)
            img = cv2.cvtColor(
                    cv2.resize(
                        cv2.imdecode(np_arr, 1), config.size),
                    cv2.COLOR_BGR2RGB)
        else:
	    img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
        frame = av.VideoFrame.from_ndarray(img, format='rgb24')
        packet = self.stream.encode(frame)
        if packet is not None:
            self.container.mux(packet)

        self.frame_count += 1

        rospy.loginfo('{} frame at {}'.format(self.frame_count, stamp)) 
        self.log.write('{} {}\n'.format(self.frame_count, stamp)) 


    def compressing(self):
        while self.is_running:
            if self.img_queue.empty(): continue

            if self.is_recording:
                # add a new frame
                stamp = self.time_queue.get()
                self.addNewFrame(stamp)

                if self.frame_count >= self.buffer_size:
                    # finsh writing a video
                    while True:
                        packet = self.stream.encode()
                        if packet is None:
                            break
                        self.container.mux(packet)
                    
                    self.container.close()
                    self.log.close()

                    self.stream = None
                    self.container = None
                    self.log = None

                    self.is_recording = False
                    self.frame_count = 0
                    self.video_count += 1

                    rospy.loginfo('finish writting video!') 
                    
            else:
                # start a new video
                rospy.loginfo('='*80) 
                rospy.loginfo('start recording a new video!') 
                stamp = self.time_queue.get()

                self.log = open(
                        config.output_dir + '{}-{}.txt'.format(self.mode, stamp), 'w')
                self.container = av.open(
                        config.output_dir + '{}-{}.mp4'.format(self.mode, stamp), 
                        mode='w', 
                        options={"preset": config.preset,
                            self.rc_method[0]: self.rc_method[1]})
                
                self.stream = self.container.add_stream('libx264', rate=config.fps)
                self.stream.width   = config.size[0]
                self.stream.height  = config.size[1]
                self.stream.pix_fmt = config.pix_fmt

                # start recording
                self.is_recording = True

                # add a new frame
                self.addNewFrame(stamp)

    
        else:
            # wait for camera set up
            pass
    
    def receive(self, img, timestamp):
        self.img_queue.put(img)
        self.time_queue.put(timestamp)
        self.received_count += 1

class Listener():

    def __init__(self):
        self.is_setup = True

        self.left_compressor = Compressor('left', config.image_is_compressed)
        self.right_compressor = Compressor('right', config.image_is_compressed)

        rospy.init_node('compress_h264', anonymous=True)

        # rospy.Subscriber(config.camera_info_topic, CameraInfo, self.camera_init)
        if config.image_is_compressed:
            rospy.Subscriber(config.left_compressed_image_topic, CompressedImage, self.left_camera_process)
            rospy.Subscriber(config.right_compressed_image_topic, CompressedImage, self.right_camera_process)
        else:
            rospy.Subscriber(config.left_image_topic, Image, self.left_camera_process)
            rospy.Subscriber(config.right_image_topic, Image, self.right_camera_process)
            

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()


    def camera_init(self, data):
        if not self.is_setup:

            config.frame_width = data.width
            config.frame_height = data.height

            rospy.loginfo('camera frame width:  {}'.format(data.width))
            rospy.loginfo('camera frame height: {}'.format(data.height))

            self.is_setup = True


    def left_camera_process(self, data):
        rospy.loginfo('received left  image at {}'.format(data.header.stamp))

        if self.is_setup:
            self.left_compressor.receive(data, data.header.stamp)
            
    
    def right_camera_process(self, data):
        rospy.loginfo('received right image at {}'.format(data.header.stamp))

        if self.is_setup:
            self.right_compressor.receive(data, data.header.stamp)


if __name__ == '__main__':
    listener = Listener()
