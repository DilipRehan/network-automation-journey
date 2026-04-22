from netmiko import ConnectHandler
from datetime import datetime

router = [
    {"device_type":"cisco_ios", "host":"192.168.138.130", "username":"admin", "password":"cisco123"}, 
    {"device_type":"cisco_ios", "host":"192.168.138.135", "username":"admin", "password":"cisco123"}, 
    {"device_type":"cisco_ios", "host":"192.168.138.136", "username":"admin", "password":"cisco123"}
]

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

for ip in router:
    try:
        connection = ConnectHandler(**ip)
        print(f"Connected to the {ip['host']} sucessfully")
        output = connection.send_command("show ip interface brief")

        file = f"Ouput{ip['host']}_{timestamp}.txt"
        with open(file,"w") as f: 
            f.write(f"Device {ip['host']}\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write("=" * 40 + "\n")
            f.write(output)
        
        print(f"Saved to {file}")
        connection.disconnect()
        
    except Exception as e:
        print(f"\nThere is issue connecting to the {ip['host']} : {e}")