# List All Users from JSONPlaceholder
# API: https://jsonplaceholder.typicode.com/users
# Goal: Display names, emails, and company names of all users.


import requests

API = requests.get("https://jsonplaceholder.typicode.com/users")
users = API.json()

for user in users:
    print(f"Name: {user["name"]}")
    print(f"Email: {user["email"]}")
    print(f"Company: {user["company"]["name"]}")
    print(f"Address: {user["address"]}")
    
    print("------------------------")
print("Total users: ", len(users))