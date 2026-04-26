
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
