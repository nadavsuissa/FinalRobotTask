media = media_ctrl
led = led_ctrl
define = rm_define

l1, l2 = 0, 255


def start():
    media.enable_sound_recognition(rm_define.sound_detection_applause)
    led.turn_off(define.armor_all)

    while True:
        media.cond_wait(define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all, l2, l1, l1, define.effect_flash)
        led.set_bottom_led(define.armor_bottom_all, l2, l1, l1, define.effect_always_on)
        # drive forward
        chassis_ctrl.set_wheel_speed(30, 30, 30, 30)

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all, l2, l2, l1, define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all, l2, l2, l1, define.effect_always_on)
        # drive backward
        chassis_ctrl.set_wheel_speed(-30, -30, -30, -30)

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all, l1, l1, l2, define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all, l1, l1, l2, define.effect_always_on)
        # drive right
        chassis_ctrl.set_wheel_speed(30, -30, -30, 30)

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all, l1, l2, l1, define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all, l1, l2, l1, define.effect_always_on)
        # drive left
        chassis_ctrl.set_wheel_speed(-30, 30, 30, -30)

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        led.set_top_led(define.armor_top_all, l2, l1, l2, define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all, l2, l1, l2, define.effect_always_on)
        chassis_ctrl.set_wheel_speed(0, 0, 0, 0)
