def analyze_packet(row):
    data = {}

    try:
        # Read values from CSV row
        data['src_ip'] = row.get('src_ip', 'unknown')
        data['dst_ip'] = row.get('dst_ip', 'unknown')
        data['packet_size'] = row.get('packet_size', 0)

        protocol = str(row.get('protocol', 'OTHER')).upper()

        if protocol == 'TCP':
            data['protocol'] = 'TCP'
        elif protocol == 'UDP':
            data['protocol'] = 'UDP'
        else:
            data['protocol'] = 'OTHER'

        return data

    except Exception as e:
        return None