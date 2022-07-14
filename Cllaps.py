

x, y = 0, 255


def start():

    media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)
    led_ctrl.turn_off(rm_define.armor_all)

    while True:
        # wait for applause
        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led_ctrl.set_top_led(rm_define.armor_top_all, y, x, x, rm_define.effect_flash)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, y, x, x, rm_define.effect_always_on)
        # drive forward
        chassis_ctrl.set_wheel_speed(30, 30, 30, 30)

        # wait for applause
        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led_ctrl.set_top_led(rm_define.armor_top_all, y, y, x, rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, y, y, x, rm_define.effect_always_on)
        # drive backward
        chassis_ctrl.set_wheel_speed(-30, -30, -30, -30)

        # wait for applause
        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led_ctrl.set_top_led(rm_define.armor_top_all, x, x, y, rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, x, x, y, rm_define.effect_always_on)
        # drive right
        chassis_ctrl.set_wheel_speed(30, -30, -30, 30)

        # wait for applause
        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led_ctrl.set_top_led(rm_define.armor_top_all, x, y, x, rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, x, y, x, rm_define.effect_always_on)
        # drive left
        chassis_ctrl.set_wheel_speed(-30, 30, 30, -30)

        # wait for applause
        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        led_ctrl.set_top_led(rm_define.armor_top_all, y, x, y, rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, y, x, y, rm_define.effect_always_on)
        chassis_ctrl.set_wheel_speed(0, 0, 0, 0)
