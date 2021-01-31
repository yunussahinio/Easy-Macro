
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from image_finder import ImageFinder
from actions import Actions
from threading import Thread
import time



class Macro(object):
    PAUSED = False
    RUNNING = False


    def __do(self):
        actions = Actions()
        
        while True:
            if not self.RUNNING: return
            if self.PAUSED: return 
            
            #region kalbi bulur  ve tıklar
            templates = ["hearth.png"]
            go_next = False
            #kapl resmini tarar
            while not go_next:
                if not self.RUNNING: return
                if self.PAUSED: return 
                
                print("PAUSED:"+ str(self.PAUSED))
                
                finder = ImageFinder(templates)
                finder_result = finder.find()
                if finder_result:#kalp resmini buldu
                    x,y = finder_result
                    #tıklar
                    actions.left_click(x,y)
                    go_next = True
                else:
                    print("resim bulunamadı")
                time.sleep(0.1)   
            #endregion
            
            #askerleri düzenler
            templates = ["hearth.png"]
            go_next = False
            while not go_next:
                if not self.RUNNING: return
                if self.PAUSED: return 
                
                print("PAUSED:"+ str(self.PAUSED))
                
                finder = ImageFinder(templates)
                finder_result = finder.find()
                if finder_result:
                    x,y = finder_result
                    actions.left_click(x,y)
                    go_next = True
                else:
                    print("resim bulunamadı")
                time.sleep(0.1)   
            #endregion
            
                
    def start_stop(self,PAUSED):
        self.PAUSED = PAUSED
        self.RUNNING = not self.RUNNING
        Thread(target = self.__do).start()
        
            
        
"""        
templates = ["hearth.png"]                  #*TARAYACAĞI RESİMLER
go_next = False                             #ELLEME LAZIM BU
while not go_next:                          #ELLEME BUDA LAZIM 
    if not self.RUNNING: return             #ELLEME DURDURMA İŞLEMİ
    if self.PAUSED: return                  #ELLEME HERŞEYİ DURDURMA İŞLEMİ
    
    finder = ImageFinder(templates)         #*RESİM ARAYICIYI ÇAĞIRIR
    finder_result = finder.find()           #*RESİMLERİ ARAR
    if finder_result:                       #*RESMİ BULDUYSA TRUE DÖNER ALTTAKİLERİ YAPAR
        x,y = finder_result                 #*BULDUĞU RESMİN X,Y KONUMUNU VERİR
        actions.left_click(x,y)             #*SOL CLICK İŞLEMİNİ YAPAR
        go_next = True                      #*BİR SONRAKİ İŞLEM İÇİN DÖNGÜDEN ÇIKAR
    else:                                   #*RESİM BULAMADI ARAMAYA DEVAMKE
        print("resim bulunamadı")           #LOG
    time.sleep(0.1)                         #*BEKLEME SÜRESİ
"""