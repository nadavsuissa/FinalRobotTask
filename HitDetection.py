def start():
    # Python
    # API：
    # Function: armor_ctrl.set_hit_sensitivity(value)
    # Parameters:
    # ● value(int): [0, 10]

    armor_ctrl.set_hit_sensitivity(9)

    while True:
        led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 255, rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 255, rm_define.effect_always_on)
        # These Commands are of type Wait, Only when occurs then the def happens:
        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_front_hit)
        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_back_hit)
        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_right_hit)
        armor_ctrl.cond_wait(rm_define.cond_armor_bottom_left_hit)


def armor_hit_detection_bottom_front(msg):
    media_ctrl.play_sound(rm_define.media_sound_attacked, wait_for_complete_flag=False)

    led_ctrl.gun_led_on()
    gun_ctrl.fire_once()
    led_ctrl.gun_led_off()
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_front, 255, 255, 255, rm_define.effect_always_on)


def armor_hit_detection_bottom_back(msg):
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 180)
    media_ctrl.play_sound(rm_define.media_sound_attacked, wait_for_complete_flag=False)
    led_ctrl.gun_led_on()
    gun_ctrl.fire_once()
    led_ctrl.gun_led_off()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 180)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_back, 255, 255, 255, rm_define.effect_always_on)


def armor_hit_detection_bottom_right(msg):
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
    media_ctrl.play_sound(rm_define.media_sound_attacked, wait_for_complete_flag=False)
    led_ctrl.gun_led_on()
    gun_ctrl.fire_once()
    led_ctrl.gun_led_off()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_right, 255, 255, 255, rm_define.effect_always_on)


def armor_hit_detection_bottom_left(msg):
    media_ctrl.play_sound(rm_define.media_sound_attacked, wait_for_complete_flag=False)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    led_ctrl.gun_led_on()
    gun_ctrl.fire_once()
    led_ctrl.gun_led_off()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)

    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 0, 0, rm_define.effect_always_on)
    time.sleep(.5)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_left, 255, 255, 255, rm_define.effect_always_on)
