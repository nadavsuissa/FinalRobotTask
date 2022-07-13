def start():
    speed = 150
    sleep_time = 1
    # Basic Init
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

    led_ctrl.set_top_led(rm_define.armor_top_right, 0, 255, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right, [2, 5, 6, 8], rm_define.effect_always_on)
    chassis_ctrl.set_wheel_speed(speed, speed, speed, speed)  # Should Be Never More then 20 in all wheels - for now lets do 300
    # Now let's got backwards:
    time.sleep(sleep_time)
    chassis_ctrl.set_wheel_speed(-speed, -speed, -speed, -speed)
    time.sleep(sleep_time)
    # By this Logic I Assume that to move sidewards should be like this:
    chassis_ctrl.set_wheel_speed(-speed, speed, speed, -speed)
    time.sleep(sleep_time)
    # Again Same Logic
    chassis_ctrl.set_wheel_speed(speed, -speed, -speed, speed)
    time.sleep(sleep_time)
    # Now that I can move forward and back and sideways, lets start turning

    chassis_ctrl.set_wheel_speed(speed, -speed, speed, -speed)

    time.sleep(sleep_time)

    chassis_ctrl.set_wheel_speed(speed, speed, speed, speed)

    time.sleep(sleep_time)
    led_ctrl.set_top_led(rm_define.armor_top_right, 255, 0, 255, rm_define.effect_always_off)
    led_ctrl.set_single_led(rm_define.armor_top_right, [1, 3, 5, 7], rm_define.effect_always_on)
    chassis_ctrl.set_wheel_speed(-speed, speed, -speed, speed)

    time.sleep(sleep_time)

    chassis_ctrl.set_wheel_speed(speed, speed, speed, speed)

    time.sleep(sleep_time)
