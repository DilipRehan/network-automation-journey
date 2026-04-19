from netmiko import ConnectHandler
import subprocess

router = {
    "device_type": "cisco_ios",
    "host": "192.168.138.130",
    "username": "admin",
    "password": "cisco123"
}

ip = {"192.168.138.130","192.168.138.2"}

def ping (ip):
    results = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    if "Destination is unreachable" in results.stdout or "Request timed out" in results.stdout:
        return False
    else:
        return True
    

def options(opt):
    try:
        if opt == "1":
            for ips in ip:   # make sure 'ip' is defined somewhere
                if ping(ips):
                    print(f"The ping for {ips} is working properly")
                else:
                    print(f"The ping for {ips} is not working properly")
            
    except Exception as e:
        print(f"Error: {e}")


def main_menu():
    while True:
        print("="*40)
        print("  Welcome to the Network Scanner  ".center(40, "*"))
        print("="*40)
        print("\nPlease select an option:")
        print("  [1] Scan the ping connectivity")
        print("  [2] Show version of the router")
        print("  [3] Full Scan")
        print("="*40)
        option = input("Enter your option (1): ").strip()
        options(option)

main_menu ()





