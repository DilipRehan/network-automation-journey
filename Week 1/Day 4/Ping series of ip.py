import subprocess

ips = ["192.168.1.1", "192.168.1.2", "8.8.8.8"]

for ip in ips:
    results = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    
    if "Destination host unreachable" in results.stdout or "Request  timed out" in results.stdout:
        print(f"{ip} - UNREACHABLE")
    else:
        print(f"{ip} - REACHABLE")
