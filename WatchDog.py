def start():
    """
    watch dog function
    """
    armor_ctrl.set_hit_sensitivity(10)
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(100)
    chassis_ctrl.set_rotate_speed(180)

    while True:
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
        led_ctrl.set_top_led(rm_define.armor_top_all, 100, 0, 100, rm_define.effect_always_on)
        chassis_ctrl.move(0)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        chassis_ctrl.rotate(rm_define.clockwise)
        time.sleep(1)


def vision_recognized_people(msg):
    """
    event of recognized people:
    shot the people and stop moving
    """
    chassis_ctrl.stop()
    gun_ctrl.fire_once()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 35)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_breath)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_breath)
    media_ctrl.play_sound(rm_define.media_sound_recognize_success)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down, 35)
