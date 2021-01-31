from image_finder import ImageFinder
from actions import Actions
import time


class Macro(object):
    STARTED = False
 
    def start_stop(self,sysTrayIcon):
        global PAUSED
        PAUSED = True
        self.STARTED = not self.STARTED
        while self.STARTED and not PAUSED:
            actions = Actions()
            kalp_template = ["hearth.png"]
            go_next = False

            while not go_next:
                finder = ImageFinder(kalp_template)
                finder_result = finder.find()
                if finder_result:
                    x,y = finder_result
                    print(x)
                    print(y)
                    actions.left_click(x,y)
                else:
                    print("resim bulunamadı")
                time.sleep(3)   