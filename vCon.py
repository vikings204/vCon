import vgamepad as vg
import keyboard as kb
# import time

print(""" __   __    ______   ______   __   __    
/\\ \\ / /   /\\  ___\\ /\\  __ \\ /\\ "-.\\ \\   
\\ \\ \\'/    \\ \\ \\____\\ \\ \\/\\ \\\\ \\ \\-.  \\  
 \\ \\__|     \\ \\_____\\\\ \\_____\\\\ \\_\\\\"\\_\\ 
  \\/_/       \\/_____/ \\/_____/ \\/_/ \\/_/ 
""")
print("vCon v1.1.0 // a virtual controller emulator\nBy Team 204 Vikings\nusage: [right shift] to toggle, [left shift] to configure, close this window to stop the emulator")
print("left joy - [WASD], right joy - [IJKL]\ndpad - arrow keys, XYAB - [FVHB]")
print("bumpers - [E][U], triggers - [Q][O]")
print("\nstarting..")

JOY_FLOAT_ON = 0.9
TRIG_FLOAT_ON = 1.0


# noinspection DuplicatedCode
def conf():
    if active:
        flipActive()
        print("conf> automatically disabled")
    print("conf> press [enter] at any setting to skip")
    global JOY_FLOAT_ON
    floatIn = input("conf> enter a float for the joystick ON position value [current " + str(JOY_FLOAT_ON) + "]: ")
    if floatIn != "":
        floatIn = float(floatIn)
        if floatIn <= 1.0 or floatIn >= -1.0:
            JOY_FLOAT_ON = floatIn
            print("conf> set to " + str(JOY_FLOAT_ON))
    global TRIG_FLOAT_ON
    floatIn = input("conf> enter a float for the trigger ON position value [current " + str(TRIG_FLOAT_ON) + "]: ")
    if floatIn != "":
        floatIn = float(floatIn)
        if floatIn <= 1.0 or floatIn >= -1.0:
            TRIG_FLOAT_ON = floatIn
            print("conf> set to " + str(TRIG_FLOAT_ON))


kb.add_hotkey('left shift', conf)

active = False
g = vg.VX360Gamepad()
joyKeys = ['w', 'a', 's', 'd', 'i', 'j', 'k', 'l']
dpadKeys = ['up', 'down', 'left', 'right']
xyabKeys = ['f', 'v', 'h', 'b']
bumpKeys = ['e', 'u']
trigKeys = ['q', 'o']
joycKeys = ['z', 'm']

joy_lx = 0.0
joy_ly = 0.0
joy_rx = 0.0
joy_ry = 0.0
trig_l = 0.0
trig_r = 0.0


def flipActive():
    global active
    active = not active
    if active:
        print("enabled")
    else:
        print("disabled")


kb.add_hotkey('right shift', flipActive)

print("started!\ndisabled")

while True:
    if active:
        # OPTIMIZE (lowers latency by not checking multiple times = 2x benefit)
        ip_joy0 = kb.is_pressed(joyKeys[0])
        ip_joy1 = kb.is_pressed(joyKeys[1])
        ip_joy2 = kb.is_pressed(joyKeys[2])
        ip_joy3 = kb.is_pressed(joyKeys[3])
        ip_joy4 = kb.is_pressed(joyKeys[4])
        ip_joy5 = kb.is_pressed(joyKeys[5])
        ip_joy6 = kb.is_pressed(joyKeys[6])
        ip_joy7 = kb.is_pressed(joyKeys[7])
        ip_dpad0 = kb.is_pressed(dpadKeys[0])
        ip_dpad1 = kb.is_pressed(dpadKeys[1])
        ip_dpad2 = kb.is_pressed(dpadKeys[2])
        ip_dpad3 = kb.is_pressed(dpadKeys[3])
        ip_xyab0 = kb.is_pressed(xyabKeys[0])
        ip_xyab1 = kb.is_pressed(xyabKeys[1])
        ip_xyab2 = kb.is_pressed(xyabKeys[2])
        ip_xyab3 = kb.is_pressed(xyabKeys[3])
        ip_bump0 = kb.is_pressed(bumpKeys[0])
        ip_bump1 = kb.is_pressed(bumpKeys[1])
        ip_trig0 = kb.is_pressed(trigKeys[0])
        ip_trig1 = kb.is_pressed(trigKeys[1])
        ip_joyc0 = kb.is_pressed(joycKeys[0])
        ip_joyc1 = kb.is_pressed(joycKeys[1])

        # left y
        # noinspection DuplicatedCode
        if ip_joy0 and not ip_joy2:
            joy_ly = JOY_FLOAT_ON
        elif ip_joy2 and not ip_joy0:
            joy_ly = -JOY_FLOAT_ON
        else:
            joy_ly = 0.0

        # left x
        if ip_joy3 and not ip_joy1:
            joy_lx = JOY_FLOAT_ON
        elif ip_joy1 and not ip_joy3:
            joy_lx = -JOY_FLOAT_ON
        else:
            joy_lx = 0.0

        # right y
        # noinspection DuplicatedCode
        if ip_joy4 and not ip_joy6:
            joy_ry = JOY_FLOAT_ON
        elif ip_joy6 and not ip_joy4:
            joy_ry = -JOY_FLOAT_ON
        else:
            joy_ry = 0.0

        # right x
        if ip_joy7 and not ip_joy5:
            joy_rx = JOY_FLOAT_ON
        elif ip_joy5 and not ip_joy7:
            joy_rx = -JOY_FLOAT_ON
        else:
            joy_rx = 0.0

        # dpad
        # noinspection DuplicatedCode
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        if ip_dpad0:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        if ip_dpad1:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        if ip_dpad2:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        if ip_dpad3:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # xyab
        # noinspection DuplicatedCode
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        if ip_xyab0:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        if ip_xyab1:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        if ip_xyab2:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        if ip_xyab3:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        # bump
        # noinspection DuplicatedCode
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        if ip_bump0:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        if ip_bump1:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # trigger
        # noinspection DuplicatedCode
        if ip_trig0:
            trig_l = TRIG_FLOAT_ON
        else:
            trig_l = 0.0
        if ip_trig1:
            trig_r = TRIG_FLOAT_ON
        else:
            trig_r = 0.0

        # joy click
        # noinspection DuplicatedCode
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        g.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        if ip_joyc0:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        if ip_joyc1:
            g.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

        g.left_joystick_float(joy_lx, joy_ly)
        g.right_joystick_float(joy_rx, joy_ry)
        g.left_trigger_float(trig_l)
        g.right_trigger_float(trig_r)
        g.update()

    # enough delay in the code, sleep is unnecessary
    # time.sleep(0.008)  # bad attempt at: effectively 125hz "polling" rate
