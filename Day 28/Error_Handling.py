# Task 5: Error Handling & Authentication
# Instructions:
# 1.	Try accessing a non-existent endpoint (e.g., https://jsonplaceholder.typicode.com/nonexistent).
# 2.	Handle the error (check status code, print an error message if request fails).
# Example Code:
# response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")

import requests
url = "https://jsonplaceholder.typicode.com/nonexistent"
response = requests.get(url)

if response.status_code == 200:
    print("Success:",response.json())
else:
    print(f"Error: status code {response.status_code}.")
