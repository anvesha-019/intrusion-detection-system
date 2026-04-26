from scapy.all import sniff, IP, TCP, UDP # sniff captures network packets
from collections import defaultdict #defaultdict is a special dictionary for counting
import datetime

LOG_FILE = "ids_log.txt"
# Track packet count per IP
ip_count = defaultdict(int)
THRESHOLD = 10 #max safe amount of packets 

def detect_intrusion(packet):  #callback function : you dont call this function manually, sniff calls it for every packet
  if packet.haslayer(IP):
    src_ip = packet[IP].src # extract src ip address 
    ip_count[src_ip]+= 1 #count packets per IP

# Detects Protocols 
    protocol = "OTHER"
    if packet.haslayer(TCP):
      protocol = "TCP"
    elif packet.haslayer(UDP):
      protocol ="UDP"

    time = datetime.datetime.now().strftime("%H:%M:%S")

    output = f"[{time}] {protocol} | {src_ip} -> Count: {ip_count[src_ip]}"
    print(output)

    with open(LOG_FILE, "a") as f:
      f.write(output + "\n")

# if no. of packets sent by one ip address are more then the threshold then the alert is generated
    if ip_count[src_ip] > THRESHOLD:
      alert = f"[ALERT] {protocol} flood from {src_ip}"
      print (alert)

      with open(LOG_FILE, "a") as f:
        f.write(alert + "\n")

sniff(prn=detect_intrusion, count=50)