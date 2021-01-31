import cv2
import numpy as np
import pyautogui
import time
import os
import utils


class ImageFinder(object):
    window_name = "March of Empires"
    threshold = 0.5  # for detecting pictures (between 0 and 1)
    image_templates = []  # filename of pics in 'templates' folder
    
    
    def __init__(self,image_templates):
        self.image_templates = image_templates
    
    def find(self):
        focused_window_name = utils.getForegroundWindowTitle()
        if self.window_name in focused_window_name:
            for image_name in self.image_templates:
                template = cv2.imread('templates/' + image_name)
                result = cv2.matchTemplate(self.__screenshot(), template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= self.threshold)
                x_list = loc[1]
                y_list = loc[0]
                print(f"{image_name}:{loc[1]}")
                if len(x_list > 0):
                    x = x_list[0]
                    y = y_list[0]
                    return x,y
        return None
    
    def __screenshot(self):
        screenshot = pyautogui.screenshot()  # gets raw image
        screenshot = np.asarray(screenshot)  # convert to numpy array in BGR
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # convert to original colors
        return screenshot

