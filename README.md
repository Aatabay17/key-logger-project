# Keylogger & Detection Demo

This project demonstrates a basic **keyboard logger (keylogger)** written in Python, and a corresponding **simple detection script** that scans for suspicious processes.

## 🎯 Goal

To show how malicious keylogging behavior works in practice, and how it can be detected using process monitoring techniques.

---

## 🧩 Components

### 1. `keylogger.py`
Captures and logs all keyboard input using the `pynput` library.

- Saves logs to `keylog.txt`
- Can run in the background
- Example log entry:
  ```plaintext
  Wed May 29 15:42:11 2025 - a
  Wed May 29 15:42:12 2025 - b
  Wed May 29 15:42:13 2025 - Backspace
2. detector.py

Scans active system processes using psutil and flags any that may behave like a keylogger.

Looks for suspicious keywords in process names or command-line arguments
Prints warning messages if something is detected
🚀 How to Run

1. Set up virtual environment (recommended)

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install dependencies

bash
pip install -r requirements.txt
3. Run the keylogger

bash
python keylogger.py
The script will start capturing keystrokes and writing them to keylog.txt.
To stop: Press Ctrl+C in the terminal.

4. Run the detector

bash
python detector.py
⚠️ Security Notes

This project is for educational purposes only
Do not run or distribute the keylogger on machines without explicit permission
Keyloggers are classified as malware outside controlled environments
📌 Example Output

From detector.py:

plaintext
[!] Suspicious process detected:
    PID: 18532
    Name: python3
    CMD: python3 keylogger.py
📁 File Structure

keylogger_project/
├── keylogger.py
├── detector.py
├── keylog.txt           # (auto-created)
├── requirements.txt
└── README.md
⚙️ Requirements

Python 3.6+
Supported OS: Windows/macOS/Linux