from adafruit_clue import clue
from time import sleep

clue_data = clue.simple_text_display(text_scale=2)
message = "This is a message.  "
clue_data[3].color = clue.SKY
tempValue = ""
while True:
    clue_data[3].text = message
    sleep(0.5)
    clue_data[3].text = ""
    sleep(0.3)
    tempValue = message[0]
    message = message[1:]+tempValue
    clue_data.show() 
    