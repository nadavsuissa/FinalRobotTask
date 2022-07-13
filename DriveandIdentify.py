def start():
    # Type of Detection
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    # Valid and Wanted Distance
    vision_ctrl.set_marker_detection_distance(3)
    # Type of Movement
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Defines of Param
    gimbal_ctrl.set_rotate_speed(20)
    chassis_ctrl.set_trans_speed(0.4)

    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 255, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 255, rm_define.effect_always_on)
    # Set Chassis Translate at 0
    chassis_ctrl.move(0)

    while True:
        # Wait for each marcker by our order, we triggered will go to correct def func
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_one)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 45)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 45)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_two)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 45)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 45)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_three)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 45)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 45)

        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_A)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_B)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_C)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
        break


def vision_recognized_marker_number_one(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.move(0)
    chassis_ctrl.stop()
    chassis_ctrl.move_with_distance(180, 0.3)



def vision_recognized_marker_number_two(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.move(0)
    chassis_ctrl.stop()
    chassis_ctrl.move_with_distance(180, 0.3)


def vision_recognized_marker_number_three(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.move(0)
    chassis_ctrl.stop()
    chassis_ctrl.move_with_distance(180, 0.3)


def vision_recognized_marker_letter_A(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.move(0)
    chassis_ctrl.stop()
    chassis_ctrl.move_with_distance(180, 0.3)


def vision_recognized_marker_letter_B(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.stop()

    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 45)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 45)
    chassis_ctrl.move(0)


def vision_recognized_marker_letter_C(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 0, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 0, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.stop()

    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 45)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 45)
    chassis_ctrl.move(0)


def vision_recognized_marker_trans_red_heart(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 255, rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 255, rm_define.effect_always_on)
    time.sleep(2)
    chassis_ctrl.stop()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 180)
