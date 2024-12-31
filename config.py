import json

def load_config(config_file='config.json'):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# Example Usage
config = load_config()
print(config["proxy_list"])  # Prints proxy list from config.json
