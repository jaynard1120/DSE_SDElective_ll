from microbit import *

first = Image("90000:09000:00900:00090:00009")
second = Image("09000:00900:00090:00009:90000")
third = Image("00900:00090:00009:90000:09000")
fourth = Image("00090:00009:90000:09000:00900")
fifth = Image("00009:90000:09000:00900:00090")
line_roll = [first,second,third,fourth,fifth]
display.show(line_roll,loop=True,delay=1000)