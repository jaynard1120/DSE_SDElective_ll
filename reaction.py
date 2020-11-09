from adafruit_clue import clue
import time
import random as randNum

clue_data = clue.simple_text_display(text_scale=2,)
score = []
clue_data[0].text="Reaction Game"
clue_data[0].color = clue.WHITE

timer = 3
while timer!=0:
    clue_data[2].text = "Instruction"
    clue_data[2].color = clue.GREEN
    clue_data[3].text = "Player A presses A"
    clue_data[3].color = clue.WHITE
    clue_data[4].text = "Player B presses B"
    clue_data[4].color = clue.WHITE
    clue_data[5].text = "Press if the number"
    clue_data[5].color = clue.BLUE
    clue_data[6].text = "  is divisible by 2"
    clue_data[6].color = clue.BLUE
    clue_data[7].text = "Maximum score of 5"
    clue_data[7].color = clue.YELLOW
    clue_data.show()
    time.sleep(1)
    clue_data[8].text = "Starts in : {:.0f} ".format(timer)
    timer-=1
    
for i in range(2,9):
    clue_data[i].text = ""

