"""
Created by: Gavin Gallant
Created on: Sep 2024
This program turns an LED on a breadboard on and off.

"""

from microbit import *


display.clear()
display.show(Image.HAPPY)


while True:
    if button_a.is_pressed():
        pin16.write_digital(1)
        display.show(Image.YES)
    if button_b.is_pressed():
        pin16.write_digital(0)
        display.show(Image.NO)
