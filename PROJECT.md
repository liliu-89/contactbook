## Python Basics Practice Project

### Concepts that we practice

+ variables
+ data types
+ built-in functions
+ if-statements
+ for loops
+ while loops
+ working with files
+ dictionaries
+ gui programming

### Vision
The Vision is to create a program, that works as a contact Book for the User.

### Features
+ list contacts
+ add contacts
+ list contacts information

### Method

Work with an agile method. Start with basic functionality. Then add extensive features and then beautify your code.

### Possible Releases

all of the numbers represent a complete release:

1. having a list that stores names
    1. hardcode contacts into that list
    2. print contacts when the program starts
2. let the user add contacts to that list
    1. now you have to let the user decide between two actions
        1. show list
        2. add contact
    2. let the user append a name to the list
3. add contacts to a local file
    1. when the user closes the program, save all current contacts to a txt file
    2. when starting the program, read all the contacts from a txt file
5. let the user add information to the contact
    1. the contact now has to be two dimensional (dictionary)
    2. when you list a user, give an index of that dictionary in the list 
    3. if user enters that index, show more information (e.g: phone, email)
6. create a GUI for the application
    
### Code Along

Follow this quick guide to code the whole program. Try to code with the instructions and without the code solution.

#### PART I

+ hardcode a list of names
+ greet the user
+ show the list of names
    + do not print the list, loop through it, so the names will appear under each other

```python
print("Welcome to your Contact Book :-)")

contacts = ["Theodor", "Steph", "Fabian"]

print("These are your contacts: \n")

for contact in contacts:
    print(contact)
```

#### PART II

+ show two options: list, add
+ you have to have two actions now - differentiate with an if statement
    + list should do the same as in Part 1
    + add should ask for an input and than, add the contact to that list
+ wrap the whole functionality in a while loop and ask if the user wants to close the program oder continue

```python
print("Welcome to your Contact Book :-)")

# hardcode
contacts = ["Theodor", "Steph", "Fabian"]


while True:
    # choose action
    action = input("What do you want to do?: (add / list)")
    
    # different actions
    if action == "list":
        print("These are your contacts: \n")
        # loops through list and prints name
        for contact in contacts:
            print(contact)
    elif action == "add":
        new_contact = input('Type in new Contact: ')
        # adds name to list
        contacts.append(new_contact)
    # not list or add
    else:
        print("Please type 'add' oder 'list'")
        continue

    # break out of the loop if y
    close = input('Close Program? (y/n)')
    if close == 'y':
        print('Thanks, see you.')
        break
```

#### PART III

+ start with adding contacts:
    + when the user wants to close the program, open the file in write mode
    + add the list to it
+ reading file when starting
    + open the contacts file in read mode
    + load data with json package so it is a searchable list

```python
import json

print("Welcome to your Contact Book :-)")

# receiving contacts from the contacts.txt
with open("contacts.txt", "r") as contacts_file:
    contacts = json.loads(contacts_file.read())

while True:
    # choose action
    action = input("What do you want to do?: (add / list)")

    # different actions
    if action == "list":
        print("These are your contacts: \n")
        # loops through list and prints name
        for contact in contacts:
            print(contact)
    elif action == "add":
        new_contact = input("Type in new Contact: ")
        # adds name to list
        contacts.append(new_contact)
    # not list or add
    else:
        print("Please type 'add' oder 'list'")
        continue

    # break out of the loop if y
    close = input("Close Program? (y/n)")
    if close == "y":
        print("Thanks, see you.")
        # add list to contacts file
        with open("contacts.txt", "w") as contacts_file:
            contacts_file.write(json.dumps(contacts))
        break
```

#### PART IV

+ type some dummy data in the contact file
+ add an index property to each contact
+ list the index plus the first name + the last name when user lists the contacts
+ when user adds a contact, create an input for each property AND count indexes so that you can add this +1 as property

```python
import json

print("Welcome to your Contact Book :-)")

# receiving contacts from the contacts.txt
with open("contacts.txt", "r") as contacts_file:
    contacts = json.loads(contacts_file.read())

while True:
    # choose action
    action = input("What do you want to do?: (add / list)")

    # different actions
    if action == "list":
        print("These are your contacts: \n")
        # loops through list and prints name
        for contact in contacts:
            print(str(contact['index']) + ": " + contact["First Name"] + " " + contact["Last Name"])
    elif action == "add":
        # create dictionary for new contact
        new_contact = {}
        new_contact["index"] = len(contacts) + 1
        new_contact["First Name"] = input("enter first name: ")
        new_contact["Last Name"] = input("enter last name: ")
        # adds dictionary to list
        contacts.append(new_contact)
    # not list or add
    else:
        print("Please type 'add' oder 'list'")
        continue

    # break out of the loop if y
    close = input("Close Program? (y/n)")
    if close == "y":
        print("Thanks, see you.")
        # add list to contacts file
        with open("contacts.txt", "w") as contacts_file:
            contacts_file.write(json.dumps(contacts))
        break
```

#### PART V 

In the making...
