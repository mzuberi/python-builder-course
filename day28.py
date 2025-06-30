import requests
import json

def fetch_data_from_api(base_url, endpoint, params=None):
    try:
        full_url = f"{base_url}/{endpoint}"
        response = requests.get(full_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"API Error: {err}")
        return None

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"File error: {e}")

# Example usage
base_url = "https://jsonplaceholder.typicode.com"
endpoint = "posts"
params = {"userId": 2}

data = fetch_data_from_api(base_url, endpoint, params)

if data:
    save_data_to_file(data, "user2_posts.json")
