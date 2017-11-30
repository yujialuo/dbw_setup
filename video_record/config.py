#!usr/bin/env python

# subsribed image topic
image_is_compressed = True
image_is_resized = False

left_image_topic = '/left_camera/pg_16492265/image_color_flipped'
left_compressed_image_topic = '/left_camera/pg_16492265/image_color_flipped/compressed'
left_camera_info_topic = '/left_camera/pg_16492265/camera_info'

right_image_topic = '/right_camera/pg_16492281/image_color_flipped'
right_compressed_image_topic = '/right_camera/pg_16492281/image_color_flipped/compressed'
right_camera_info_topic = '/right_camera/pg_16492281/camera_info'

# maximum number of frames in one video
max_frames = 1000
#max_frames = 60

# fps in video
fps = 30

# default camera info
#frame_height = 1080
#frame_width = 1080

# io directory
#output_dir = '/media/psf/repository/BDD_data/car/'
#output_dir = '/media/bdd/bdd_ssd_0/BDD_data/car/0929/'
output_dir = './'

# output video name
out = 'test.mp4'

# target frame size
size = (2048, 2048)

# rate control method
rc_method = 'crf 25'

# pix format
pix_fmt = 'yuv420p'

# preset mode
preset = 'ultrafast'
