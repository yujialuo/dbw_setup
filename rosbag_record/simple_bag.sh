rosbag record --split --duration 5m -b 30720  /nmea_sentence /vehicle/brake_cmd /vehicle/brake_info_report /vehicle/brake_report /vehicle/gear_report /vehicle/gps/fix /vehicle/gps/time /vehicle/gps/vel /vehicle/imu/data_raw /vehicle/joint_states /vehicle/misc_1_report /vehicle/req_accel /vehicle/sonar_cloud /vehicle/steering_cmd /vehicle/steering_report /vehicle/surround_report /vehicle/suspension_report /vehicle/throttle_cmd /vehicle/throttle_info_report /vehicle/throttle_report /vehicle/tire_pressure_report /vehicle/turn_signal_cmd /vehicle/wheel_position_report /vehicle/wheel_speed_report /vehicle/twist /vehicle/twist_controller/parameter_descriptions /vehicle/twist_controller/parameter_updates /vehicle/wheel_speed_report /xsens/fix /xsens/imu/data /xsens/imu/mag /xsens/imu_data_str /xsens/time_reference &
python ~/Desktop/camera_video/src/video.py 