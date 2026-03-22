from scapy.all import sniff
from analyzer import analyze_packet
from detector import detect_anomaly

captured_data = []

def process_packet(packet):
    data = analyze_packet(packet)
    
    if data:
        alerts = detect_anomaly(data)
        
        data['alerts'] = alerts
        
        print(data)
        captured_data.append(data)

def start_sniffing():
    print("Starting packet capture...")
    sniff(prn=process_packet, count=15)