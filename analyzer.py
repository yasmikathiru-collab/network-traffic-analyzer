from scapy.layers.inet import IP, TCP, UDP

def analyze_packet(packet):
    data = {}

    # Check if IP layer exists
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        
        data['src_ip'] = ip_layer.src
        data['dst_ip'] = ip_layer.dst
        data['packet_size'] = len(packet)

        # Check protocol
        if packet.haslayer(TCP):
            data['protocol'] = 'TCP'
        elif packet.haslayer(UDP):
            data['protocol'] = 'UDP'
        else:
            data['protocol'] = 'OTHER'

    return data