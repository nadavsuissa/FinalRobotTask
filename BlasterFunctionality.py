# Blaster functionality:
def start():
    # Not Fun Enough,
    # Must For Free non dependent movement
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    gun_ctrl.set_fire_count(5)  # Burst Of Gel Beads

    gimbal_ctrl.set_rotate_speed(400)  # Rotate Speed
    shoot()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    shoot()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 180)
    shoot()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    shoot()
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 180)
    shoot()


def shoot():
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 40)
    # Fire but not Automatic:
    led_ctrl.gun_led_on()
    for count in range(5):
        gun_ctrl.fire_once()
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_breath)
    gun_ctrl.fire_once()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=False)
    gun_ctrl.stop()
    led_ctrl.set_top_led(rm_define.armor_top_all, 0, 0, 0, rm_define.effect_breath)
    time.sleep(1)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down, 40)
    led_ctrl.gun_led_off()
