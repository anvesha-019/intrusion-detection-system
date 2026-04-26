
---

# 📁 3. Intrusion Detection System (IDS) — README.md

```markdown
# Intrusion Detection System (IDS)

## 📌 Description
A Python-based Intrusion Detection System that monitors network traffic in real time and detects suspicious activity based on packet frequency thresholds.

## 🚀 Features
- Real-time packet monitoring
- Tracks packet count per IP
- Detects potential flooding attacks
- Protocol identification (TCP/UDP)
- Timestamped logging of traffic and alerts

## 🛠️ Tools & Technologies
- Python
- Scapy

## ⚙️ How It Works
The system captures network packets using Scapy and tracks the number of packets received from each source IP. If the number of packets from a single IP exceeds a defined threshold, an alert is triggered indicating potential malicious activity.

## ▶️ How to Run
```bash
pip install scapy
python ids.py

## Output
<img width="1164" height="857" alt="Screenshot 2026-04-26 105936" src="https://github.com/user-attachments/assets/02408cc7-b70e-4e8e-80b7-ebba6848bb79" />
<img width="934" height="381" alt="Screenshot 2026-04-26 105916" src="https://github.com/user-attachments/assets/3ae6c9fd-2e41-490d-8b78-03044b9f9d1a" />
