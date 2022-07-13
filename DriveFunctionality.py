def start():
    # Basic Init
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    led_ctrl.set_top_led(rm_define.armor_top_right, 0, 255, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right, [2, 5, 6, 8], rm_define.effect_always_on)
    chassis_ctrl.set_wheel_speed(40, 40, 40, 40)  # Should Be Never More then 20 in all wheels - for now lets do 40
    # Now let's got backwards:
    time.sleep(5)
    chassis_ctrl.set_wheel_speed(-40, -40, -40, -40)
    time.sleep(5)
    # By this Logic I Assume that to move sidewards should be like this:
    chassis_ctrl.set_wheel_speed(-40, 40, 40, -40)
    time.sleep(5)
    # Again Same Logic
    chassis_ctrl.set_wheel_speed(40, -40, -40, 40)
    time.sleep(5)
    # Now that I can move forward and back and sideways, lets start turning

    chassis_ctrl.set_wheel_speed(40, -40, 40, -40)

    time.sleep(5)

    chassis_ctrl.set_wheel_speed(40, 40, 40, 40)

    time.sleep(5)
    led_ctrl.set_top_led(rm_define.armor_top_right, 255, 0, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right, [1, 3, 5, 7], rm_define.effect_always_on)
    chassis_ctrl.set_wheel_speed(-40, 40, -40, 40)

    time.sleep(5)

    chassis_ctrl.set_wheel_speed(40, 40, 40, 40)

    time.sleep(5)
