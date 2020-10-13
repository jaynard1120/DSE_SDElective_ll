from adafruit_clue import clue
from time import sleep


clue_data = clue.simple_text_display(title="Message Streamer", title_scale=2,title_color=(255,0,0))

message1 = "This message moves from right to left...  "
message2 = "This is message moves from left to right...  "
message3 = "This message blinks"
clue_data[1].color = clue.YELLOW
clue_data[3].color = clue.WHITE
clue_data[5].color = clue.SKY
tempValue = ""
counter = 0
while True:
    clue_data[1].text = message1
    clue_data[3].text = message2
    clue_data[5].text = message3
    clue_data.show()

    message3 = "This message blinks" if counter % 2 == 0 else ""
    tempValue = message1[0]
    message1 = message1[1:]+tempValue
    tempValue = message2[len(message2)-1]
    message2 = tempValue+message2[:-1]

    counter+=1
    sleep(0.3)