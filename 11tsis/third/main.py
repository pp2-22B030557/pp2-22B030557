import psycopg2
import re
from psycopg2 import errors
import csv

from database import conn
from crud import *



def validate_phone_number(phone_number):
    phone_number = phone_number.replace(" ", "")
    
    pattern = "^(\+7|8)[0-9]{9,11}$"
    match = re.match(pattern, phone_number)
    
    if match and match.group() == phone_number:
        return True
    else:
        return False

def start():
    # print("1. Add contact\n2. Add phone number for contact")
    cycle = True
    while cycle:
        print()
        type_of_action = int(input("1. Add contact\n2. Add phone number for contact\n3. Print all contacts\n4. Print all Phone numbers\n5. Get contant by id\n6. Get phone number by id\n7. Update contact\n8. Update phone number\n9. Add contacts from csv\n10. Add phone numbers from csv\n11. Delete contact\n12. Exit\n"))
        if type_of_action == 1:
            name = input("Enter a name: ")
            email = input("Enter email: ")

            contact = get_contact_by_name(name)
            if(contact is None):
                create_contact(name, email)
            else:
                update_contact(contact[0], name, email)

        if type_of_action == 2:
            number = input("Enter a number: ")
            number_valid = validate_phone_number(number)
            contact_id = int(input("Enter id of contact: "))
            if number_valid:
                try:
                    create_phone_number(contact_id, number)
                except errors.ForeignKeyViolation as e:
                    print(f"Error: Contact with this id: {contact_id} does not exist")
            else:
                print("Incorrect phone format")

        if type_of_action == 3:
            page_count = int(input("Enter a number of paginations: "))
            contact = get_all_contacts()
            count = 1
            print()
            print("Name   Email   Phone")
            for i in contact:
                phones = get_phone_numbers(i[0])
                # print(phones)
                for phone in phones:
                    print(i[1], "  ",i[2], "  ",phone[1])
                    if count % page_count == 0:
                        count = 0
                        key = input('Enter "q" to exit or eny key to next: ')
                        if(key == "q"):
                            start()
                    count += 1

        if type_of_action == 4:
            data = get_all_phone_numbers()
            print()
            print("id   Phone   contact_id")
            for i in data:
                print(i[0], "  ",i[1], "  ",i[2])

        if type_of_action == 5:
            id = input("Enter id of contact: ")
            data = get_contact(id)
            print("id   Name   Email")
            print(data[0], "  ",data[1], "  ",data[2])

        if type_of_action == 6:
            id = input("Enter id of phone number: ")
            data = get_phone_numbers(id)
            print("id   Phone   contact_id")
            print(data[0], "  ",data[1], "  ",data[2])

        if type_of_action == 7:
            id = input("Enter id of contact: ")
            name = input("Enter a name: ")
            email = input("Enter email: ")
            update_contact(id, name, email)

        if type_of_action == 8:
            id = input("Enter id of phone number: ")
            number = input("Enter a number: ")
            update_phone_number(id, number)

        if type_of_action == 9:
            with open("myFile0.csv") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        cur.execute("INSERT INTO contacts (id, name, email) VALUES (%s, %s, %s)", (row['id'], row['name'], row['email']))
                    except errors.UniqueViolation as e:
                        print(e)
                    conn.commit()
        
        if type_of_action == 10:
            with open("myFile1.csv") as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    try:
                        cur.execute("INSERT INTO phone_numbers (id, number, contact_id) VALUES (%s, %s, %s)", (row['id'], row['number'], row['contact_id']))
                    except errors.UniqueViolation as e:
                        print(e)
                    except errors.ForeignKeyViolation as e:
                        print(e)
                    
                    conn.commit()

        if type_of_action == 11:
            name = input("Enter name of contact to delte: ")
            contact = get_contact_by_name(name)
            if(contact is None):
                print("Account not found")
            else:
                delete_contact(contact[0])

        if type_of_action == 12:
            cycle = False

if __name__ == '__main__':
    start()