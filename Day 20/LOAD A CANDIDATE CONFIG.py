from napalm import get_network_driver

driver = get_network_driver("ios")

device = driver(
    hostname="192.168.138.137",
    username="admin",
    password="cisco123",
    optional_args={"secret": "cisco123"},
)

device.open()

# Load candidate config
device.load_merge_candidate(filename="candidate.txt")
print("Candidate config loaded successfully!")

# Discard for now — don't apply yet
device.discard_config()
print("Config discarded — not applied.")

device.close()