
import requests

def fetch_data_from_api(base_url, endpoint, params=None):
    try:
        full_url = f"{base_url}/{endpoint}"
        response = requests.get(full_url, params=params)

        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    return None

# Example: Get posts from user 1
base_url = "https://jsonplaceholder.typicode.com"
endpoint = "posts"
params = {"userId": 1}

data = fetch_data_from_api(base_url, endpoint, params)
if data:
    for post in data[:3]:
        print(f"- {post['title']}")
🧠 What You Learned
Built a clean, safe API function

Used raise_for_status() for better error handling

Created a base for future apps (like AI bots!)
                                

