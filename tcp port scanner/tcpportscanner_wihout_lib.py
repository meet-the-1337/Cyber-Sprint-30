# Day 2 — Python CLI Tool #1: Port Scanner Build a raw TCP port scanner in Python from scratch. No libraries that do the work for you. Takes a target IP and port range, returns open ports with banners. Must have CLI args via argparse, error handling, and clean output. Push to GitHub with a README.

import argparse
import socket

parser = argparse.ArgumentParser(description="Simple Port Scanner")

parser.add_argument("target", help="Target IP Address")
parser.add_argument("-s", "--start", type=int, help="Start Port",required=True)
parser.add_argument("-e", "--end", type=int, help="End Port",required=True)

args = parser.parse_args()

print(f"Target: {args.target}")
print(f"Start Port: {args.start}")
print(f"End Port: {args.end}")
open_ports = []
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            try:
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()  # Receive banner (if any)
                print(f"[+] Port {port} is OPEN - Banner: {banner}")
            except:
                print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

print("-- Scanning Ports --")
print(f"Scanning ports from {args.target}")
print("---------------------")

for port in range(args.start, args.end+1):
    scan_port(args.target, port)

print("---------------------")
print("Scan Complete")
print(f"open ports found  :{len(open_ports)}")

if open_ports:
    print("Open Ports:", ",".join(map(str, open_ports)))