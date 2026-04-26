from netmiko import ConnectHandler

router = {
    "device_type":"cisco_ios",
    "host":"192.168.138.130",
    "username":"admin",
    "password":"cisco123",
    "secret":"cisco123"
}

connection = ConnectHandler(**router)
connection.enable()
output = connection.send_command("show ip interface brief", use_textfsm=True)

print("="*45)
print("INTERFACES - STRUCTURED DATA")
print("="*45)

for intf in output:
    print(f"Interface : {intf['interface']}")
    print(f"IP        : {intf['ip_address']}")
    print(f"Status    : {intf['status']}")
    print(f"Protocol  : {intf['proto']}")
    print("="*30)

connection.disconnect()