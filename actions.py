import pyautogui

class Actions:
    def __init__(self):
        pyautogui.FAILSAFE = False
        
    def right_click(self,x,y):
        pyautogui.rightClick(x+2, y+2) 
        # mouse_x, mouse_y = pyautogui.position()
        # pyautogui.moveTo(mouse_x, mouse_y)

    def left_click(self,x,y):
        pyautogui.click(x+2, y+2) 
        # mouse_x, mouse_y = pyautogui.position()
        # pyautogui.moveTo(mouse_x, mouse_y)
    
    def drag(self,x_distance,y_distance, duration = 0.5):
        pyautogui.drag(x_distance, y_distance, duration)
        #pyautogui.(x+2, y+2) 
        # pyautogui.moveTo(mouse_x, mouse_y)