from microbit import *
from time import sleep

dot = "00000:00000:00000:00000:00000"

currentIndex = 0
incrementBy = [1,6,-1,-6]
index = 0
times = 3
numberOfindex = 4


while True:
    if numberOfindex == 1:
        times = 3

    for i in range(times):
        for j in range(numberOfindex):   
            index = 0 if index > 3 else index
            dotList = list(dot)
            dotList[currentIndex] = '9'
            display.show(Image(''.join(dotList)))

            currentIndex += incrementBy[index] if currentIndex != 14 else currentIndex
            sleep(0.5)
            if currentIndex == 28 and numberOfindex == 1:
                numberOfindex = 5
                currentIndex = 0
                index = -1
                times = 4
                break

        index = index+1
    numberOfindex = numberOfindex-1

    
    if times > 2:
        times = times-1