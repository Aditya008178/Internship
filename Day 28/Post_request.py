# Task 4: POST Request (Sending Data)
# Instructions:
# 1.	Use the same API to create a new post.
# 2.	Send a JSON payload with:
# {
#   "title": "New Post",
#   "body": "This is a test post.",
#   "userId": 1
# }
# 3.	Print the response (should include the new post with an ID).
# Expected Output:
# New Post: {'title': 'New Post', 'body': 'This is a test post.', 'userId': 1, 'id': 101}

import requests
url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "New Post",
    "body": "This is a test post.",
    "userId": 1
}

response = requests.post(url,json=payload)

print("New Post: ",response.json())


