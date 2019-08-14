import json #json will help us seamlessly convert between a list and a string

print('Welcome to your contactbook')

# receiving contacts from the contacts.txt
with open("contacts.txt", "r") as contacts_file:
    contacts = json.loads(contacts_file.read())

#print contacts when the program starts
print('Your contacts are listed below')
for contact in contacts:
    print(str(contact["index"]) + ": " + contact["First Name"] + " " + contact["Last Name"])

#now you have to let the user decide between two actions
while True:
    choice = input("Add contact or show list? (add / list) ")
    if choice == "add": #add contact
        new_contact = {}
        new_contact["index"] = len(contacts) + 1
        new_contact["First Name"] = input("enter first name: ")
        new_contact["Last Name"] = input("enter last name: ")
        contacts.append(new_contact)

    elif choice == "list": #show list
        for contact in contacts:
            print(str(contact["index"]) + ": " + contact["First Name"] + " " + contact["Last Name"])

    else:
        print('Please type "add" or "list"')
        continue

# break out of the loop if y
    close = input("Close program? (y / n)")
    if close == "y":
        print("Goodbye!")
        # add list to contacts file
        with open("contacts.txt", "w") as contacts_file:
            contacts_file.write(json.dumps(contacts))
            break