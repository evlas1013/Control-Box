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

b8 = digitalio.DigitalInOut(board.GP8)
b8.switch_to_input(pull=digitalio.Pull.DOWN)

b9 = digitalio.DigitalInOut(board.GP9)
b9.switch_to_input(pull=digitalio.Pull.DOWN)

b10 = digitalio.DigitalInOut(board.GP10)
b10.switch_to_input(pull=digitalio.Pull.DOWN)

b11 = digitalio.DigitalInOut(board.GP11)
b11.switch_to_input(pull=digitalio.Pull.DOWN)

b12 = digitalio.DigitalInOut(board.GP12)
b12.switch_to_input(pull=digitalio.Pull.DOWN)

b13 = digitalio.DigitalInOut(board.GP13)
b13.switch_to_input(pull=digitalio.Pull.DOWN)

b14 = digitalio.DigitalInOut(board.GP14)
b14.switch_to_input(pull=digitalio.Pull.DOWN)

b15 = digitalio.DigitalInOut(board.GP15)
b15.switch_to_input(pull=digitalio.Pull.DOWN)

b16 = digitalio.DigitalInOut(board.GP16)
b16.switch_to_input(pull=digitalio.Pull.DOWN)

b17 = digitalio.DigitalInOut(board.GP17)
b17.switch_to_input(pull=digitalio.Pull.DOWN)

b18 = digitalio.DigitalInOut(board.GP18)
b18.switch_to_input(pull=digitalio.Pull.DOWN)

b19 = digitalio.DigitalInOut(board.GP19)
b19.switch_to_input(pull=digitalio.Pull.DOWN)


buttonDelay = 50
currentDelay = 0
lastPressed = -1
while True:
    time.sleep(0.01)
    currentDelay += 1
    print(lastPressed)

    if b0.value and (lastPressed != 0 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.ZERO)
        lastPressed = 0
        currentDelay = 0
        continue

    if b1.value and (lastPressed != 1 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.ONE)
        lastPressed = 1
        currentDelay = 0
        continue

    if b2.value and (lastPressed != 2 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.TWO)
        lastPressed = 2
        currentDelay = 0
        continue

    if b3.value and (lastPressed != 3 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.THREE)
        lastPressed = 3
        currentDelay = 0
        continue

    if b4.value and (lastPressed != 4 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.FOUR)
        lastPressed = 4
        currentDelay = 0
        continue

    if b5.value and (lastPressed != 5 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.FIVE)
        lastPressed = 5
        currentDelay = 0
        continue

    #Buttons 6 and 7 will be "continuous" and have no cooldown
    if b6.value:
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.SIX)
        lastPressed = 6
        currentDelay = 0
        continue

    if b7.value:
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.SEVEN)
        lastPressed = 7
        currentDelay = 0
        continue

    if b8.value and (lastPressed != 8 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.EIGHT)
        lastPressed = 8
        currentDelay = 0
        continue

    if b9.value and (lastPressed != 9 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_ALT, Keycode.NINE)
        lastPressed = 9
        currentDelay = 0
        continue

    if b10.value and (lastPressed != 10 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.ZERO)
        lastPressed = 10
        currentDelay = 0
        continue

    if b11.value and (lastPressed != 11 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.ONE)
        lastPressed = 11
        currentDelay = 0
        continue

    if b12.value and (lastPressed != 12 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.TWO)
        lastPressed = 12
        currentDelay = 0
        continue

    if b13.value and (lastPressed != 13 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.THREE)
        lastPressed = 13
        currentDelay = 0
        continue

    if b14.value and (lastPressed != 14 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.FOUR)
        lastPressed = 14
        currentDelay = 0

    if b15.value and (lastPressed != 15 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.FIVE)
        lastPressed = 15
        currentDelay = 0
        continue

    if b16.value and (lastPressed != 16 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.SIX)
        lastPressed = 16
        currentDelay = 0
        continue

    if b17.value and (lastPressed != 17 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.SEVEN)
        lastPressed = 17
        currentDelay = 0
        continue

    if b18.value and (lastPressed != 18 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.EIGHT)
        lastPressed = 18
        currentDelay = 0
        continue

    if b19.value and (lastPressed != 19 or currentDelay > buttonDelay):
        k.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.LEFT_ALT, Keycode.NINE)
        lastPressed = 19
        currentDelay = 0
        continue

