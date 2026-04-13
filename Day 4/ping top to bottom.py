import subprocess

ip_prefix = "192.168.1."

print("=" *40)

for i in range(1, 10):
    ip = ip_prefix + str(i)
    results = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    
    if "Destination host unreachable" in results.stdout or "Request timed out" in results.stdout:
        print(f"* {ip} - UNREACHABLE❕")
    else:
        print(f"* {ip} - REACHABLE ✅")




