from netmiko import ConnectHandler


router = {
    "device_type":"cisco_ios",
    "host":"192.168.138.130",
    "username":"admin",
    "password":"cisco123",
    "secret":"cisco123",
}

connection = ConnectHandler(**router)
connection.enable()

output = connection.send_command("show version", use_textfsm=True)
print("=" * 45)
print("DEVICE VERSION -STRUCTURED DATA")
print("="*45)
print(f"Hostname     : {output[0]['hostname']}")
print(f"Version      : {output[0]['version']}")
print(f"Uptime       : {output[0]['uptime']}")
print(f"Model        : {output[0]['hardware']}") 



connection.disconnect()