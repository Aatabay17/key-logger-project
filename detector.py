import psutil
import time

# Список подозрительных ключевых слов, по которым ищем процессы
suspicious_keywords = ['keylogger', 'pynput', 'keylog', 'listener']

def is_suspicious(proc):
    """
    Проверяет, содержит ли имя процесса или его аргументы
    подозрительные ключевые слова.
    
    proc - объект процесса psutil.Process
    Возвращает True, если процесс подозрительный, иначе False.
    """
    try:
        # Получаем имя процесса и командную строку в нижнем регистре
        name = proc.name().lower()
        cmdline = ' '.join(proc.cmdline()).lower()
        # Проверяем каждое ключевое слово
        for keyword in suspicious_keywords:
            if keyword in name or keyword in cmdline:
                return True
    except (psutil.AccessDenied, psutil.ZombieProcess, 
psutil.NoSuchProcess):
        # Если нет доступа или процесс уже завершён - игнорируем
        pass
    return False

def scan_for_keyloggers():
    """
    Перебирает все запущенные процессы и выводит информацию
    о подозрительных процессах.
    """
    print("Scanning running processes for suspicious behavior...\n")
    found = False
    # Проходим по всем процессам, запрашиваем сразу нужные атрибуты
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

