# Get a Random Dog Image
# API: https://dog.ceo/api/breeds/image/random
# Goal: Fetch and print the image URL (bonus: open it in the browser with webbrowser.open())

import webbrowser, requests

URL = requests.get("https://dog.ceo/api/breeds/image/random")

image_url = URL.json()["message"]
print(image_url)
webbrowser.open(image_url)

