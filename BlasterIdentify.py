
def start():
    """
    Blaster fire example function
    """

    def exampleidentify():
        robot_ctrl.set_mode(rm_define.robot_mode_free)

        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        vision_ctrl.set_marker_detection_distance(1)

        while True:
            vision_ctrl.cond_wait(rm_define.cond_recognized_people)

            while True:

                gimbal_ctrl.set_rotate_speed(55)
                # Rotate sound
                media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate, wait_for_complete_flag=False)
                # Flash
                led_ctrl.set_flash(rm_define.armor_all, 4)
                led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)

                gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 35)

                led_ctrl.set_flash(rm_define.armor_all, 9)
                led_ctrl.set_top_led(rm_define.armor_top_all, 0, 255, 255, rm_define.effect_flash)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 0, 255, 255, rm_define.effect_flash)

                media_ctrl.play_sound(rm_define.media_sound_shoot, wait_for_complete_flag=True)
                media_ctrl.play_sound(rm_define.media_sound_shoot, wait_for_complete_flag=True)

                commands_exit = random.randint(1, 2)

                if commands_exit == 1:
                    continue
                elif commands_exit == 2:
                    led_ctrl.set_flash(rm_define.armor_all, 4)
                    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
                    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)

                    gimbal_ctrl.recenter()

                    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 255, 0, rm_define.effect_breath)
                    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 255, 1, rm_define.effect_breath)
                    break
    # Call
    exampleidentify()
