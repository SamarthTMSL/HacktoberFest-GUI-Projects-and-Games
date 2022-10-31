import pyautogui as pt
import time
#user input here
limit = input("Enter limit:")
message = input("Enter message:")
i = 0
time.sleep(5)

#Aditya Seth.
#adityaseth.cse@gmail.com
while i < int(limit):
    pt.typewrite(message)
    # the message is written where -
    # the cursor belongs      

    pt.press("enter")

    i += 1
    
    
