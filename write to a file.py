import subprocess

ips = ["8.8.8.8"]

for ip in ips:
    results =subprocess.run(["ping", "-n", "2", ip], capture_output=True, text=True)
    if "Request timed out" in results.stdout or "Destination host unreachable" in results.stdout:
        print(f"{ip} is UNREACHABLE")
    else:
        print(f"{ip} is REACHABLE")

file = open ("text.txt", "w")
file.write("Hello Network Engineer\n")
file.write("This is my first \n")
file.close()
