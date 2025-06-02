import psutil
import time

# Подозрительные ключевые слова
suspicious_keywords = ['keylogger', 'pynput', 'keylog', 'listener']

def is_suspicious(proc):
    try:
        name = proc.name().lower()
        cmdline = ' '.join(proc.cmdline()).lower()
        for keyword in suspicious_keywords:
            if keyword in name or keyword in cmdline:
                return True
    except (psutil.AccessDenied, psutil.ZombieProcess, 
psutil.NoSuchProcess):
        pass
    return False

def scan_for_keyloggers():
    print("Scanning running processes for suspicious behavior...\n")
    found = False
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if is_suspicious(proc):
            print(f"[!] Suspicious process detected:")
            print(f"    PID: {proc.pid}")
            print(f"    Name: {proc.name()}")
            print(f"    CMD: {' '.join(proc.cmdline())}\n")
            found = True

    if not found:
        print("✅ No suspicious processes found.")

if __name__ == "__main__":
    scan_for_keyloggers()

