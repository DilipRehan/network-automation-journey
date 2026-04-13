import subprocess

def ping_ip(ips):
    results = subprocess.run (["ping", "-n", "1", ips], capture_output=True, text=True)
    if "Destination host unreachable" in results.stdout or "Request timed out" in results.stdout:
        return False
    else:
        return True
    
file = open("ip_list.txt", "r")
ips = file.read().splitlines()
file.close()


print ("==" * 40)
print("PINGING FROM FILE")
print("=" * 40)

for ip in ips:
    if ping_ip(ip):
        print(f"{ip} - REACHABLE")
    else:
        print(f"{ip} - UNREACHABLE")

print("=" *40)

