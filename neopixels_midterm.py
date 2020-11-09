from adafruit_circuitplayground import cp
from time import sleep

cp.pixels.brightness = 1
ndx = 9
while True:
    for i in range(0,10):
        if ndx<0:
            ndx = 9
        cp.pixels[ndx] = (255,255,255)
        sleep(1)
        
        if(ndx == 0 or ndx == 5):
            cp.pixels[ndx] = (255,255,255)
            ndx-=1
            continue
        if ndx == 4 or ndx == 9:
            cp.pixels[0] = (0,0,0)
            cp.pixels[5] = (0,0,0)
        sleep(1)
        cp.pixels[ndx] = (0,0,0)
        



        ndx -=1
