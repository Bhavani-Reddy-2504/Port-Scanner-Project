import socket

target = input("Enter IP Address: ")

common_ports = {
    21:"FTP",
    22:"SSH",
    23:"TELNET",
    25:"SMTP",
    53:"DNS",
    80:"HTTP",
    443:"HTTPS"
}

print(f"\nScanning {target}...\n")

for port in common_ports:

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"{common_ports[port]} (Port {port}) OPEN")

    scanner.close()

print("\nScan Completed")