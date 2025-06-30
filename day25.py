import requests

def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Here's a cute dog for you:")
        print(data["message"])
    else:
        print("Failed to fetch a dog image. Try again later.")

get_random_dog_image()
