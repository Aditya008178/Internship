# 8.	Contact Book
# o	Create a dictionary contacts with 3 people’s names as keys and their phone numbers as values.
# o	Add a new contact.
# o	Update one contact’s number.
# o	Delete one contact.


contacts = {"Aditya" : 8857858968, "Piyush" : 7620007358, "Swapnil" : 7030036662}
print(f"Contacts : {contacts}")

contacts["Tejas"] = 9423575365 #Added a new contact
print(f"Contacts after adding a new contact : {contacts}")

contacts["Aditya"] = 9923520356 #Updated one contact's number
print(f"Contacts after updating one contact's number : {contacts}")

del contacts["Piyush"] #Deleting one contact number
print(f"Contacts after deleting one contact's number : {contacts}")