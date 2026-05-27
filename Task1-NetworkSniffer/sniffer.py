from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def show_packet(packet):
    if IP in packet:
        time = datetime.now().strftime("%H:%M:%S")
        src = packet[IP].src
        dst = packet[IP].dst
        
        if TCP in packet:
            print(f"[{time}] TCP | {src}:{packet[TCP].sport} --> {dst}:{packet[TCP].dport}")
        elif UDP in packet:
            print(f"[{time}] UDP | {src}:{packet[UDP].sport} --> {dst}:{packet[UDP].dport}")
        elif ICMP in packet:
            print(f"[{time}] ICMP | {src} --> {dst}")
        else:
            print(f"[{time}] OTHER | {src} --> {dst} | Proto: {packet[IP].proto}")

print("CodeAlpha Network Sniffer Started...")
print("Capturing packets... Open Chrome and visit any website")
print("Press Ctrl+C to stop\n")
sniff(prn=show_packet, store=0)