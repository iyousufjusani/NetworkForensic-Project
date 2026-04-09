import pyshark

def detect_brute_force(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    failed_attempts = {}

    for packet in cap:
        if hasattr(packet, 'tcp') and hasattr(packet, 'ip'):
            src_ip = packet.ip.src

            if src_ip in failed_attempts:
                failed_attempts[src_ip] += 1
            else:
                failed_attempts[src_ip] = 1

    print("\n--- Analysis Result ---\n")

    for ip, count in failed_attempts.items():
        print(f"{ip} → {count} attempts")

        if count > 5:
            print(f"⚠️ - Possible brute-force attack from {ip}\n")

detect_brute_force('remote_access.pcap')