from adafruit_circuitplayground import cp
from time import sleep
cp.pixels.brightness = 1


color = 0
index = 0
temp = 0
i = 0
while True:
    
    index = cp.light // 32 
    temp = (cp.light // 32)* 32
    
    i = i if i < 10 else 0

    if i == index:
        color = 255 if int(255 * (cp.light - temp)/ 32) > 255 else int(255 * (cp.light - temp)/ 32)
        color = 0 if int(255 * (cp.light - temp)/ 32) < 0 else color
        cp.pixels[index] = (color,color,color)
    
    if i < index:
        cp.pixels[i] = (255,255,255)

    elif i > index:
        cp.pixels[i] = (0,0,0)
    
    i = i + 1