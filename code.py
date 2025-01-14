# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board 
import digitalio 
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

buttonB = digitalio.DigitalInOut(board.button_B)
buttonB.direction = digitalio.direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

print(dir(board))
print(' ')
print(dir(digitalio))
print(' ')
print(dir(digitalio.DigitalInOut))
print(' ')
print(dir(led))
print(' ')
print(led.direction)
# print (dir(digitalio.Pull))
x=5
print(dir(x))
print(type(x))
print(x)
while True:
    led.value = buttonB.value
    print(buttonB.value)
    time.sleep(.2)

print("hello world!")
