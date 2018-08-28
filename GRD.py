import pyautogui
import time
import cv2

############# 

def write(p, w):
	pyautogui.click(p)
	pyautogui.typewrite(w)
	pyautogui.press('enter')


bloc = 530 , 748
n = input()

write(bloc, n)
