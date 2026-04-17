import subprocess


def ping_devices(ips):
    results = subprocess.run(["ping", "-n", "2", ips], capture_output=True, text=True)
    if "Destination host unreachable" in results.stdout or "Request timed out" in results.stdout:
        return False
    else:
        return True
    

output = open("ping_results.txt", "w")
output.write(f"Network scan results \n")


# Load IPs from file
file = open("ip_list.txt", "r")
ips = file.read().splitlines()


for ip in ips:
    if ping_devices(ip):
        line = f"Reachable {ip} "
    else:
        line = f"Unreachable {ip}"
    output.write(line+ "\n")

