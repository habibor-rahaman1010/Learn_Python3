import pyautogui
from time import *

sleep(5)
text = 'What is Lorem Ipsum?'

for i in range(3):
    pyautogui.write(text, interval=.10)
    pyautogui.press('enter')
