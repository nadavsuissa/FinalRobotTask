# Blaster functionality:
def start():
    # Fire but not Automatic:
    for count in range(5):
        led_ctrl.gun_led_on()
        gun_ctrl.fire_once()
        led_ctrl.gun_led_off()

    # Not Fun Enough,
    # Must For Free non dependent movement
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    gun_ctrl.set_fire_count(5)  # Burst Of Gel Beads

    # Function: gimbal_ctrl.set_rotate_speed(speed)
    # Parameters:
    # ● speed(float): [0, 540] ° / s

    gimbal_ctrl.set_rotate_speed(180)  # Rotate Speed
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 40)
    gun_ctrl.fire_once()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=False)
    gun_ctrl.stop()
    time.sleep(1)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down, 40)
    time.sleep(1)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 40)
    gun_ctrl.fire_once()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=False)
    gun_ctrl.stop()
    time.sleep(1)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down, 40)
    gun_ctrl.fire_once()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=False)
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 180)
    gun_ctrl.fire_once()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=False)
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
    gun_ctrl.fire_once()
    media_ctrl.play_sound(rm_define.media_sound_shoot, wait_complete_flag=False)
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 180)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)
