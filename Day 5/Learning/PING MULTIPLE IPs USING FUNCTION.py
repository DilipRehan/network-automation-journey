import subprocess

ips =["8.8.8.8", "192.168.1.1", "1.1.1.1", "192.168.1.2", "8.8.4.4"]

def ping_device(ip):
    results = subprocess.run (["ping", "-n", "1", ip], capture_output=True, text=True)
    if "Destination host unreachable" in results.stdout or "Request timed out" in results.stdout:
        return False
    else:
        return True
    

print ("=" * 40)
for ip in ips:
     if ping_device(ip):
          print(f"{ip} - REACHABLE ✅")
     else:
         print(f"{ip} - UNREACHABLE ❕")
          

    
    
    
    







