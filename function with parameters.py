def device_Info(hostname, ip, vendor):
    print(f"Hostname: {hostname}")
    print(f"IP: {ip}")
    print(f"Venor: {vendor}")
    print("=" * 25)

device_Info("R1", "192.168.1.1", "Cisco")
device_Info("R2", "192.168.1.2", "Juniper")
device_Info("R3", "192.168.1.3", "Fortinet")
