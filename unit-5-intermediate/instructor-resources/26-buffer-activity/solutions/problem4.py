def get_contact(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "You don't have that person's number!"


# If you would like to test the example code, uncomment the code below

# contacts = {
#   "Carly": "333-3333",
#   "Blondie": "444-4444",
#   "Jenny": "867-5309"
# }
# name = "Jenny"
# phone_number = get_contact(contacts, name)

# print("The phone number of", name, "is", phone_number)
