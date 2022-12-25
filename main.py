import pyautogui as pg
from time import sleep

whatToWrite = input("What to write:")
sleepTimeBefore = int(input("Sleep Time before executing:"))
spamDelay = int(input("Spam Delay (leave blank for default):"))
keyboardToPress = input("Keyboard to press (leave as blank for default)")
howMuch = int(input("How much time to repeat (leave blank for no range repeat)"))
if(keyboardToPress == None):
    keyboardToPress = "enter"
if(howMuch == None):
    howMuch = "whileTrue"
if(spamDelay == None):
    spamDelay = 1

sleep(sleepTimeBefore)

def main():
    pg.typewrite(whatToWrite)
    pg.press(keyboardToPress)

if(howMuch == "whileTrue"):
    while True:
        main()
        sleep(spamDelay)
else:
    for i in range(howMuch):
        main()
        sleep(spamDelay)
