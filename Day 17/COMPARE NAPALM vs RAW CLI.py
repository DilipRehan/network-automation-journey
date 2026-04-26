from napalm import get_network_driver
from netmiko import ConnectHandler

print("=" * 45)
print("NAPALM OUTPUT - Structured")
print("=" * 45)

driver = get_network_driver("ios")

device = driver(
    hostname = "192.168.138.130",
    username = "admin",
    password = "cisco123",
    optional_args={"secret":"cisco123"}
)

try:
    device.open()
    routes = device.get_route_to("10.10.10.0/24")
    for prefix, data in routes.items():
        print(f"Prefix    : {prefix}")
        print(f"Protocol  : {data[0]['protocol']}")
        print(f"Routing table : {data[0]['routing_table']}")
        print(f"Next Hop      : {data[0]['next_hop']}")
        print(f"Active        : {data[0]['current_active']}")

        #static = "default" if data[0]['routing_table'] else "down"
        #print(static)
    device.close()

    print("\n" + "=" * 45)
    print("NETMIKO OUTPUT - Raw CLI")
    print("="* 45)


#from here onwards the netmiko starts
    router = {
        "device_type":"cisco_ios",
        "host":"192.168.138.130",
        "username":"admin",
        "password":"cisco123",
        "secret":"cisco123",
    }

    connection = ConnectHandler(**router)
    connection.enable()

    output = connection.send_command("show ip route 10.10.10.0")
    print(output)
    connection.disconnect()

except Exception as e:
    print(f"Somethig went wrong! {e}")