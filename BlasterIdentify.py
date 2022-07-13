# Make Robomaster fire his blaster every time he sees a person. Set the vision marker
# detection distance from 0.5 to 3 for farther distances.

def start():
    # Blaster fire example function:

    def exampleidentify():
        # Non Dependent
        robot_ctrl.set_mode(rm_define.robot_mode_free)

        # Python
        # API：
        # Function: vision_ctrl.enable_detection(function_enum)
        # vision_ctrl.disable_detection(function_enum)
        # Parameters:
        # ● function_enum(enum):
        # ■ rm_define.vision_detection_marker
        # ■ rm_define.vision_detection_pose
        # ■ rm_define.vision_detection_car
        # ■ rm_define.vision_detection_people

        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        vision_ctrl.set_marker_detection_distance(1)

        while True:
            vision_ctrl.cond_wait(rm_define.cond_recognized_people)

            while True:
                randgimbal_speed = random.randint(20, 100) // 30
                randup = random.randint(1, 55) // 20

                gimbal_ctrl.set_rotate_speed(randgimbal_speed)

                media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate, wait_for_complete_flag=False)

                led_ctrl.set_flash(rm_define.armor_all, 4)

                led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)

                gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, randup)

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