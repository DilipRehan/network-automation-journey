import subprocess

ips =["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for i in ips:
    subprocess.run(f"ping {i}")