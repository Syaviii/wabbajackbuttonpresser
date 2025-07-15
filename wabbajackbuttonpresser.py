import pyautogui
import cv2
import numpy as np
import time
import keyboard
from PIL import ImageGrab

def find_and_click_button(button_image_path, confidence=0.8):
    button_image = cv2.imread(button_image_path, cv2.IMREAD_UNCHANGED)
    if button_image.shape[2] == 4:
        button_image = cv2.cvtColor(button_image, cv2.COLOR_BGRA2BGR)
    button_image_gray = cv2.cvtColor(button_image, cv2.COLOR_BGR2GRAY)

    while True:
        if keyboard.is_pressed('ctrl+alt+s'):
            print("no more buttons :c")
            break

        screen = np.array(ImageGrab.grab())
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, button_image_gray, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= confidence:
            button_center = max_loc[0] + button_image.shape[1]//2, max_loc[1] + button_image.shape[0]//2

            pyautogui.moveTo(button_center)
            pyautogui.click()

        time.sleep(0.6)

button_image_path = r'WHEREVER THE NEXUS MODS DOWNLOAD BUTTON SCREENSHOT IS'
find_and_click_button(button_image_path)
