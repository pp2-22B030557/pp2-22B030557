import psycopg2

from database import conn


cur = conn.cursor()


def create_contact(name, email):
    cur.execute("INSERT INTO contacts (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()

def get_contact(contact_id):
    cur.execute("SELECT * FROM contacts WHERE id = %s", (contact_id,))
    return cur.fetchone()

def get_contact_by_name(name):
    cur.execute("SELECT * FROM contacts WHERE name = %s", (name,))
    return cur.fetchone()

def get_all_contacts():
    cur.execute("SELECT * from contacts")
    return cur.fetchall()

def update_contact(contact_id, name, email):
    cur.execute("UPDATE contacts SET name = %s, email = %s WHERE id = %s", (name, email, contact_id))
    conn.commit()

def delete_contact(contact_id):
    cur.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    conn.commit()

def create_phone_number(contact_id, number):
    cur.execute("INSERT INTO phone_numbers (contact_id, number) VALUES (%s, %s)", (contact_id, number))
    conn.commit()

def get_phone_numbers(contact_id):
    cur.execute("SELECT * FROM phone_numbers WHERE contact_id = %s", (contact_id,))
    return cur.fetchall()

def get_all_phone_numbers():
    cur.execute("SELECT * from phone_numbers")
    return cur.fetchall()

def update_phone_number(phone_number_id, number):
    cur.execute("UPDATE phone_numbers SET number = %s WHERE id = %s", (number, phone_number_id))
    conn.commit()

def delete_phone_number(phone_number_id):
    cur.execute("DELETE FROM phone_numbers WHERE id = %s", (phone_number_id,))
    conn.commit()

# cur.close()
# conn.close()