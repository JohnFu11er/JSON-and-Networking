import json

with open('network_device_data.json', mode='rt') as file:
    device_data = json.load(file)

for device, config in device_data.items():
    print(f"Name: {config['name']}")
    for interface in config['interfaces']:
        print("  {}".format(interface))
        for key, value in config['interfaces'][interface].items():
            print("    " + key + " : " + value)
    print()