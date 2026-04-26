from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(
    hostname ="192.168.138.130",
    username = "admin",
    password = "cisco123",
    optional_args={"secret":"cisco123"},
)

device.open()

facts = device.get_facts()
print("="*45)
print("DEVICE FACTS")
print("=" * 45)
print(f"Hostname  :{facts['hostname']}")
print(f"Vendor    :{facts['vendor']}")
print(f"OS        :{facts['os_version']}")


interfaces = device.get_interfaces()
print("\n"+ "=" * 45 )
print("INTERFACES")
print("="*45)
for name, details in interfaces.items():
    status = "UP" if details["is_up"] else "DOWN !"
    print(f"{name:20} {status}")




routes = device.get_route_to("10.10.10.0/24")
print("\n"+ "=" *45)
print("ROUTE - 10.10.10.0/24")
print("=" * 45)
for prefix, data in routes.items():
    print(f"Prefix   : {prefix}")
    print(f"Next Hop : {data[0]['next_hop']}")
    print(f"Protocol : {data[0]['protocol']}")
    print(f"Active   : {data[0]['current_active']}")



device.close()
