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

output = connection.send_command("show ip interface brief", use_textfsm=True)


print("="* 45)
print("INTERFACE HEALTH CHECK")
print("=" * 45)

up = []
down = []

for intf in output:
    if intf["status"] == "up":
        up.append(intf["interface"])
        print(f"{intf['interface']:20} {intf['ip_address']}")
    else:
        down.append(intf['interface'])
        print(f" ! {intf['interface']:20} DOWN")

print("=" * 45)
print(f"UP {len(up)}")
print(f"DOWN {len(down)}")
print("=" * 45)
