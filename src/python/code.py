import requests
import os
from datetime import datetime
import json

# Assuming you have the API's base URL
base_url = "https://example.com/api/customers"
some_id = "12345"  # Example some ID

# Use os.environ.get to safely get environment variables
username = os.environ.get('API_USER')
password = os.environ.get('API_PASS')

# Headers for the request
headers = {
    "Content-Type": "application/json"
}

# Data you want to patch, converted to JSON
# For example, updating the timestamp
data = {
    "timestamp": datetime.now().isoformat(),
    # Add other fields you want to patch here
}

# Make the PATCH request
response = requests.patch(f"{base_url}/{some_id}", headers=headers, data=json.dumps(data),
                          auth=(username, password))

# Check the response
if response.status_code == 200:
    print("Successfully patched the customer info.")
    print(response.json())  # Assuming the response contains JSON data
else:
    print(f"Failed to patch customer info. Status code: {response.status_code}")
    print(response.text)  # To see the error message

