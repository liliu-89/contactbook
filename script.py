import json #json will help us seamlessly convert between a list and a string

print('Welcome to your contactbook')

#hardcode contacts into that list
#contacts = ["Alex", "Basti", "Chris"]
# receiving contacts from the contacts.txt
with open("contacts.txt", "r") as contacts_file:
    contacts = json.loads(contacts_file.read())

#print contacts when the program starts
print('Your contacts are listed below')
for contact in contacts:
    print(contact)

#now you have to let the user decide between two actions
while True:
    choice = input("Add contact or show list? (add / list) ")
    if choice == "add": #add contact
        add_name = input("Add a Name: ")
        contacts.append(add_name)
        print("Thank you. " + add_name + " was added to your contacts.")
    elif choice == "list": #show list
        for contact in contacts:
            print(contact)

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