import subprocess

def ping_device(ip):
    result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    
    if "Destination host unreachable" in result.stdout or "Request timed out" in result.stdout:
        return False
    else:
        return True
    

ip = "8.8.8.8"

if ping_device(ip):
    print(f"{ip} - REACHABLE ✅")
else:
    print(f"{ip} - NOT REACHABLE ❌")