from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(
    hostname = "192.168.138.130",
    username = "admin",
    password = "cisco123",
    optional_args={"secret":"cisco123"},
)

device.open()


facts = device.get_facts()

print("Device Facts:")
print(f"Hostname     :{facts['hostname']}")
print(f"Vendor       :{facts['vendor']}")
print(f"Model        :{facts['model']}")
print(f"OS Version   :{facts['os_version']}")
print(f"Uptime       :{facts['uptime']} seconds")

device.close()