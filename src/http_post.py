"""
Create a config file for the server

configs/http_config.json
{
    "https":{
        "server":" 	https://webhook.site/c246134a-badf-44b2-971a-795ec3b0b974"
        "username":"",
        "password":""
    },
}
"""

import json
import time
from pico_lte.utils.status import Status
from pico_lte.core import PicoLTE
from pico_lte.common import debug

# Initialize Pico LTE
picoLTE = PicoLTE()

def read_config():
    """
    Reads the config.json file and returns the configuration dictionary.
    """
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            debug.info(f"Configuration file loaded successfully: {config}")
            return config
    except FileNotFoundError:
        debug.error("config.json file not found. Ensure the file is uploaded to the device.")
        return None
    except json.JSONDecodeError as e:
        debug.error(f"Error parsing config.json: {e}")
        return None

# Step 1: Load configuration
config = read_config()
if not config:
    debug.error("Failed to load configuration. Exiting...")
    exit()

# Step 2: Register network
debug.info("Registering network...")
result = picoLTE.network.register_network()
if result["status"] != Status.SUCCESS:
    debug.error(f"Network registration failed: {result}")
    exit()
debug.info("Network registered successfully.")

# Step 3: Set HTTP context ID
debug.info("Setting HTTP context ID...")
result = picoLTE.http.set_context_id()
if result["status"] != Status.SUCCESS:
    debug.error(f"Failed to set context ID: {result}")
    exit()
debug.info("HTTP context ID set successfully.")

# Step 4: Check PDP ready
debug.info("Checking PDP readiness...")
result = picoLTE.network.get_pdp_ready()
if result["status"] != Status.SUCCESS:
    debug.error(f"PDP not ready: {result}")
    exit()
debug.info("PDP is ready.")

# Step 5: Set server URL
server_url = config["https"]["server"]
debug.info(f"Setting server URL to: {server_url}")
result = picoLTE.http.set_server_url(server_url)
if result["status"] != Status.SUCCESS:
    debug.error(f"Failed to set server URL: {result}")
    exit()
debug.info("Server URL set successfully.")

# Step 6: Send POST request
debug.info("Sending a POST request...")
payload_dict = {"message": "PicoLTE HTTP Post Example"}
payload_json = json.dumps(payload_dict)
debug.info(f"Payload to send: {payload_json}")

result = picoLTE.http.post(data=payload_json)
if result["status"] != Status.SUCCESS:
    debug.error(f"POST request failed: {result}")
    exit()
debug.info("POST request sent successfully. Awaiting response...")

# Step 7: Read the response
time.sleep(5)
debug.info("Reading response from server...")
result = picoLTE.http.read_response()
if result["status"] == Status.SUCCESS:
    debug.info("POST request succeeded.")
    debug.info(f"Response from server: {result['response']}")
else:
    debug.error(f"Failed to read response: {result}")

debug.info("Script completed.")


