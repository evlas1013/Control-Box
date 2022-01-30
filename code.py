import board
import usb_hid
import digitalio
import time
from adafruit_hid.Keyboard import Keyboard
from adafruit_hid.keycode import Keycode
print("running")
k = Keyboard(usb_hid.devices)

b0 = digitalio.DigitalInOut(board.GP0)
b0.switch_to_input(pull=digitalio.Pull.DOWN)

b1 = digitalio.DigitalInOut(board.GP1)
b1.switch_to_input(pull=digitalio.Pull.DOWN)

b2 = digitalio.DigitalInOut(board.GP2)
b2.switch_to_input(pull=digitalio.Pull.DOWN)

b3 = digitalio.DigitalInOut(board.GP3)
b3.switch_to_input(pull=digitalio.Pull.DOWN)

b4 = digitalio.DigitalInOut(board.GP4)
b4.switch_to_input(pull=digitalio.Pull.DOWN)

b5 = digitalio.DigitalInOut(board.GP5)
b5.switch_to_input(pull=digitalio.Pull.DOWN)

b6 = digitalio.DigitalInOut(board.GP6)
b6.switch_to_input(pull=digitalio.Pull.DOWN)

b7 = digitalio.DigitalInOut(board.GP7)
b7.switch_to_input(pull=digitalio.Pull.DOWN)


buttonDelay = 50
currentDelay = 0
lastPressed = -1
while True:
    currentDelay += 1

    if b0.value and (lastPressed != 0 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.ZERO)
        lastPressed = 0
        currentDelay = 0

    if b1.value and (lastPressed != 1 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.ONE)
        lastPressed = 1
        currentDelay = 0

    if b2.value and (lastPressed != 2 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.TWO)
        lastPressed = 2
        currentDelay = 0

    if b3.value and (lastPressed != 3 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.THREE)
        lastPressed = 3
        currentDelay = 0

    if b4.value and (lastPressed != 4 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.FOUR)
        lastPressed = 4
        currentDelay = 0

    if b5.value and (lastPressed != 5 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.FIVE)
        lastPressed = 5
        currentDelay = 0

    if b6.value:
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.SIX)
        lastPressed = 6
        currentDelay = 0

    if b7.value:
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.SEVEN)
        lastPressed = 7
        currentDelay = 0

    time.sleep(0.01)

