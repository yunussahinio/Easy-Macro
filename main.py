import pyautogui
import utils
import keyboard
import shortcuts


from macros import attack, defense

from infi.systray import SysTrayIcon

"""
variables
"""
PAUSED = False
attack = attack.Macro()
defense = defense.Macro()



"""
functions
"""
def pause():
    PAUSED = True
    attack.start_stop(PAUSED)
    defense.start_stop(PAUSED)
    

"""
shortcuts
"""
#TODO kısayollar çalışmıyor
keyboard.add_hotkey(shortcuts.PAUSE, pause)
keyboard.add_hotkey(shortcuts.ATTACK, attack.start_stop, args=(PAUSED,))
keyboard.add_hotkey(shortcuts.DEFENSE, defense.start_stop, args=(PAUSED,))



"""
system tray icon menus
"""
menu_options = (
    (f"Attack ({shortcuts.ATTACK})", None, lambda _: attack.start_stop(PAUSED)),
    (f"Defense ({shortcuts.DEFENSE})", None, lambda _: defense.start_stop(PAUSED)),
    (f"Pause ({shortcuts.PAUSE})", None, lambda _: pause()),
    
)


"""
system tray icon
"""
systray = SysTrayIcon("icon.ico", "March of Empires Bot", menu_options)
systray.start()
