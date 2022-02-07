import pyautogui
import time

comments = ['a'] #to write comment 

time.sleep(2)  #to start a commet time 

for i in range (100) : # if in range (100) => you has 100ment 
    pyautogui.typewrite(comments) 
    pyautogui.typewrite ('\n')
    time.sleep (3)

