import subprocess

ips =["192.168.1.1", "8.8.8.8"]

def ping_ip(ip):
    if ip.startswith("8.8"):
        return True
    else:
        return False
    
for single_ip in ips:
    if ping_ip(single_ip):
        results = subprocess.run (["ping", "-n", "5", single_ip], capture_output=True, text= True)

        if "Reply from" in results.stdout:
            print(f"{single_ip} - REACHABLE ✅")
        else:
            print(f"{single_ip} - NOT REACHABLE ❌")