import subprocess

ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "8.8.8.8"]

for ip in ips:
    results = subprocess.run (["ping", "-n", "1", ip], capture_output=True, text=True)
    print(results.stdout)