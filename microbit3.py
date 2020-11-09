from microbit import *
from time import sleep


while True:

    brightnessControl = (display.read_light_level() // 10) * 10
    brightness = display.read_light_level() - brightnessControl
    positionControl = display.read_light_level() // 50
    xposition = (display.read_light_level()-(positionControl*50))// 10
    yposition = 4 - positionControl

    for i in range(5):

        
        if i > yposition:
            for j in range(5):
                display.set_pixel(j, i, 9)

        if i < yposition:
            for j in range(5):
                display.set_pixel(j, i, 0)
        
        if i == yposition:
            
            for j in range(5):
                if j < xposition:
                    display.set_pixel(j, i, 9)
                if j > xposition:
                    display.set_pixel(j, i, 0)

    if yposition > -1:
        display.set_pixel(xposition, yposition, brightness)