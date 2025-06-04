# Keylogger and Detection System - Practical Cybersecurity Demonstration

## Overview
This project provides a practical demonstration of both offensive and defensive cybersecurity mechanisms by simulating a common real-world threat: a keylogger. A keylogger is surveillance software designed to record every keystroke made by a user, often without their consent or awareness.  

We implement a basic keylogger that captures user input and logs it to a file. In parallel, a lightweight detection script scans running system processes for signs of malicious behavior, specifically targeting known indicators associated with keyloggers.

The project is an educational tool aimed at cybersecurity students and practitioners, helping them understand how such threats operate, how they can be deployed, and most importantly, how they can be detected and neutralized. By simulating both attacker and defender roles, it offers insight into offensive tactics and defensive techniques.

---

## Motivation
Keyloggers are commonly used by cybercriminals due to their stealthy nature and ability to capture sensitive data like login credentials, personal messages, and financial information. They appear in phishing attacks, spyware campaigns, and advanced persistent threats (APTs). Despite their simplicity, keyloggers remain highly effective.

This project aims to understand both the technical mechanisms and real-world implications of keyloggers by building a prototype from scratch. It also explores challenges in detecting such threats, especially when they masquerade as legitimate processes.

**Note:** This project is for educational purposes only and is not intended to promote malicious activity.

---

## Project Components

### 1. `keylogger.py` - Keystroke Logging Module  
- **Keyboard Monitoring:** Uses `pynput.keyboard` to listen continuously for keyboard events, capturing both printable and special keys (Enter, Backspace, Shift, etc.).  
- **Timestamped Logging:** Records every keystroke with timestamps using the `time` module, appending data to `keylog.txt`.  
- **Silent Background Execution:** Runs in the background with minimal console output and no GUI windows or alerts.  
- **macOS Accessibility Check:** Uses AppleScript (`osascript`) to verify Accessibility permissions required to monitor keyboard events on macOS. If not granted, the keylogger does not run.

### 2. `detector.py` - Process Monitoring and Keylogger Detection  
- **Process Enumeration:** Uses `psutil` to iterate over all running processes, gathering process name, command-line arguments, and PID.  
- **Keyword-Based Heuristic Matching:** Checks process metadata for suspicious keywords such as `"keylogger"`, `"pynput"`, `"listener"`.  
- **Threat Flagging and Reporting:** Flags suspicious processes and prints warnings with PID, name, and command line for manual analysis.

---

## Attack Demonstration

Running `keylogger.py` starts monitoring keyboard activity in real time. It captures all key presses, including letters, numbers, symbols, and special keys, logging them to `keylog.txt` with timestamps.

**Sample keylog.txt excerpt:**

Wed May 29 15:42:11 2025 - a
Wed May 29 15:42:12 2025 - b
Wed May 29 15:42:13 2025 - Backspace
Wed May 29 15:42:14 2025 - c
Wed May 29 15:42:15 2025 - 1
Wed May 29 15:42:16 2025 - 2
Wed May 29 15:42:17 2025 - 3
Wed May 29 15:42:18 2025 - Enter


This log allows reconstruction of sensitive input, including passwords and confidential messages. Input corrections like Backspace are also logged, increasing data accuracy.

The keylogger operates silently, without GUI or alerts, starting only if Accessibility permissions are granted on macOS.

---

## Detection Mechanism

The `detector.py` script scans active system processes to identify potential keylogger activity:

1. **Process Enumeration:**  
   Uses `psutil.process_iter()` to retrieve all active processes and their metadata (PID, name, command line).

2. **Signature-Based Detection:**  
   Compares process name and command line against suspicious keywords:
   ```python
   suspicious_keywords = ['keylogger', 'pynput', 'keylog', 'listener']

Matches flag the process as potentially dangerous.

3. Alerting:
If a match is found, the script outputs:

[!] Suspicious process detected:
    PID: 8083
    Name: python3
    CMD: python3 keylogger.py

This enables users or admins to investigate or terminate the process.

Technical Stack

Language: Python 3
Libraries:
pynput – keyboard input monitoring
psutil – process monitoring
Platform: macOS (tested with required Accessibility permissions)
Implementation Highlights

Permission checks to ensure necessary Accessibility rights are granted before running.
Real-time keystroke logging with timestamps.
Cross-platform compatible code with macOS-specific security checks.
Detection script designed for extensibility with behavioral or signature-based rules.
Ethical Considerations

Created strictly for educational and ethical research.
No real user data was compromised.
Scripts must never be deployed in real environments or against users without explicit consent.
Results

Keystrokes are logged reliably and accurately.
Detection system successfully identifies running keylogger processes.
Both attacker and defender roles function as intended.
Conclusion

This project offers a hands-on exploration of keylogging threats and defenses. It highlights the importance of system visibility and basic monitoring to detect malicious activity. Although simple, it provides a solid foundation for advanced security research such as behavioral detection and automated countermeasures.

Future Work

Add cross-platform support (Windows, Linux).
Implement log encryption and remote data exfiltration simulation.
Enhance detection with anomaly-based or advanced signature-based techniques.