def start():
    """"
    identify numbers markers
    """
    # base definitions
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    chassis_ctrl.set_trans_speed(0.3)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    vision_ctrl.set_marker_detection_distance(3)

    # identify marker 1
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    chassis_ctrl.move_with_time(0, 2)
    gun_ctrl.fire_once()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 30)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)

    # identify marker 2
    vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_two)
    chassis_ctrl.move_with_time(0, 2)
    gun_ctrl.fire_once()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 0)

    # identify marker 3
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_three)
    chassis_ctrl.move_with_time(0, 2)
    gun_ctrl.fire_once()
