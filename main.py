import pyautogui,time

time.sleep(3)

file = open("song.txt", 'r');

for line in file:
    pyautogui.typewrite(line);
    pyautogui.press("Enter");
    time.sleep(1)

file.close();


    

    

