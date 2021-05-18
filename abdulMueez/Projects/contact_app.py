import json

def create_contact():
    name = input("Please enter name: ")
    print(" ")
    email = input("Please enter email: ")
    print(" ")
    contact = input("Please enter contact: ")
    contact_data = {
        "name":name,
        "email":email,
        "contact":contact,
    }

    data = str(contact_data)


    with open("contact_app.txt", 'a') as f:
        f.write(data)
        f.write("\n")


def delete_contact():
    contact_to_delete = input("Enter name of contact you want to delete: ")
    data = ""

    with open("contact_app.txt", 'r') as f:
        content = f.readlines()
        data = content

    a = []
    for i in data:
        contact = i.replace("'",'"')

        contact = json.loads(contact)


        a.append(contact)
    
    print(a)

    
    for i in range(len(a)):
        if a[i]['name'].lower() == contact_to_delete.lower():
            del a[i]


    with open("contact_app.txt", 'w') as f:
        f.write("")
            
        for j in a:
            with open("contact_app.txt", 'a') as f:
                f.write(str(j))
                f.write("\n")


def update_contact():
    contact_to_update = input("Enter name of contact you want to update: ")
    what_to_update = input("What do you want to update (name, email, phone): ")
    updated_value = input(f"what is the new {what_to_update}: ")
    
    data = ""

    with open("contact_app.txt", 'r') as f:
        content = f.readlines()
        # print(content)
        data = content

    a = []
    for i in data:
        contact = i.replace("'",'"')

        contact = json.loads(contact)


        a.append(contact)

    
    for i in range(len(a)):
        if a[i]['name'].lower() == contact_to_update.lower():
            a[i][what_to_update] = updated_value
            break
    b = 0
    
    for j in a:
        if b <1:
            with open("contact_app.txt", 'w') as f:
                f.write(str(j))
                f.write("\n")

            b+=1
        else:
            with open("contact_app.txt", 'a') as f:
                f.write(str(j))
                f.write("\n")

def search_contact():
    contact_to_delete = input("Enter name of contact you want to delete: ")

    data = ""

    with open("contact_app.txt", 'r') as f:
        content = f.readlines()
        data = content

    
    for i in data:
        contact = i.replace("'",'"')

        contact = json.loads(contact)
        
        if contact_to_delete.lower() == contact['name'].lower():
            print(contact)

def list_contact():
    data = ""

    with open("contact_app.txt", 'r') as f:
        content = f.readlines()
        data = content

    a = []
    for i in data:
        contact = i.replace("'",'"')

        contact = json.loads(contact)


        print("--------------------------------------------------------------")
        print(f"{contact}")
        print("--------------------------------------------------------------")


def welcome():
    print("----------------------------------------------------")
    print("Hello, welcome to PY CONTACT APP!!!                 |")
    print("----------------------------------------------------")
    print(" ")

    user_input = input("What do you want to do: \n\n 1. Create a new contact. \n\n 2. Delete Contact \n\n 3. Update Contact \n\n 4. List Saved Contacts \n\n Enter here: ")
    

    if int(user_input) == 1:
        create_contact()
    elif int(user_input) == 2:
        delete_contact()
    elif int(user_input) == 3:
        update_contact()
    elif int(user_input) == 4:
        list_contact()
    else:
        print("Invalid Input")

welcome()