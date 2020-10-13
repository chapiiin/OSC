import sqlite3
from sqlite3 import Error
import functools

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

#function to create a table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.close()
    except Error as e:
        print(e)

#function to insert data into a table
def insert_data(conn, insert_data_sql):
    try:
        c = conn.cursor()
        c.execute(insert_data_sql)
        conn.commit()
        print("Successfully populated table with data.\n")
        c.close()
    except Error as e:
        print(e)
#function to display all current inventory items
def display_inventory(conn):
    try:
        print("\n")
        print("Welcome to the Online Shopping Center. Below is our current available inventory.\n")
        print("__________________________________________________________\n")
        c = conn.cursor()
        print("\n---HOUSE HOLD ITEMS---")
        print("(Name, Description, Price, Available Quantity)\n\n")
        c.execute("SELECT * FROM household_items;")
        print(c.fetchall())
        print("\n")
        print("\n---BOOKS---")
        print("(Name, Description, Price, Available Quantity)\n\n")
        c.execute("SELECT * FROM books;")
        print(c.fetchall())
        print("\n")
        print("\n---SMALL ELECTRONICS---")
        print("(Name, Description, Price, Available Quantity)\n\n")
        c.execute("SELECT * FROM small_electronics_items;")
        print(c.fetchall())
        print("\n")
        print("\n---TOYS---")
        print("(Name, Description, Price, Available Quantity)\n\n")
        c.execute("SELECT * FROM toys;")
        print(c.fetchall())
        print("\n")
    except Error as e:
        print(e)

#function to properly setup the database
def setup_database():
    database = (r"C:\sqlite\db\osc_system.db")

    #Create the inventory category tables
    household_items_table = """CREATE TABLE IF NOT EXISTS household_items (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INT NOT NULL
    );"""

    books_table = """CREATE TABLE IF NOT EXISTS books (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INT NOT NULL
    );"""

    toys_table = """CREATE TABLE IF NOT EXISTS toys (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INT NOT NULL
    );"""

    small_electronics_table = """CREATE TABLE IF NOT EXISTS small_electronics_items (
        name TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INT NOT NULL
    );"""


       ##populate books table with data
    books1 = """INSERT INTO books (name, description, price, quantity)
    VALUES ('IT', 'A 1986 horror novel by American author Stephen King', 22.35, 25)"""
    books2 = """INSERT INTO books (name, description, price, quantity)
    VALUES ('The Great Gatsby', 'A 1925 novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the fictional
    towns of West Egg and East Egg on prosperous Long Island in the summer of 1922', 18.56, 25)"""
    books3 = """INSERT INTO books (name, description, price, quantity)
    VALUES ('1984', ' Imagination of what a future society might look like at its worst written by George Orwell', 15.99, 25)"""
    books4 = """INSERT INTO books (name, description, price, quantity)
    VALUES ('Lord of the Flies', 'A novel based on what happens when a group of boys who are stranded on a deserted island have to learn how to survive', 8.99, 25)"""
    books5 = """INSERT INTO books (name, description, price, quantity)
    VALUES ('War and Peace', 'A novel by the Russian author Leo Tolstoy based on the French invasion of Russia and the impact of the
    Napoleonic era on Tsarist society through the stories of five Russian aristocratic families', 13.97, 25)"""


        ##populate household items table with data
    household_item1 = """INSERT INTO household_items (name, description, price, quantity)
    VALUES ('Paper Towels', 'Bounty paper towels', 3.50, 25)"""
    household_item2 = """INSERT INTO household_items (name, description, price, quantity)
    VALUES ('Vacuum', 'Dyson bagless upright vacuum, black', 54.00, 25)"""
    household_item3 = """INSERT INTO household_items (name, description, price, quantity)
    VALUES ('Mini-fridge', '1.7 cubic ft single door mini fridge, black', 79.00, 25)"""
    household_item4 = """INSERT INTO household_items (name, description, price, quantity)
    VALUES ('Curtains', 'Mainstays textured solid curtain panel, black', 5.88, 25)"""
    household_item5 = """INSERT INTO household_items (name, description, price, quantity)
    VALUES ('Table', '6ft centerfold table, white', 42.00, 25)"""


         ##populate small electronic items table with data
    se_item1 = """INSERT INTO small_electronics_items (name, description, price, quantity)
    VALUES ('KODAK PIXPRO Digital Camera', '16MP 40X Optical Zoom HD720p video, Red', 149.00, 25)"""
    se_item2 = """INSERT INTO small_electronics_items (name, description, price, quantity)
    VALUES ('Prepaid Smartphone', 'Straight Talk SAMSUNG Galaxy A01, 16GB, Black', 55.25, 25)"""
    se_item3 = """INSERT INTO small_electronics_items (name, description, price, quantity)
    VALUES ('Roku Smart LED TV', 'JVC 50" Class 4K UHD 2160p HDR Roku Smart LED TV LT-50MAW595', 202.10, 25)"""
    se_item4 = """INSERT INTO small_electronics_items (name, description, price, quantity)
    VALUES ('Bluetooth Speaker', 'QFX 8-in Portable Party Bluetooth PA Loudspeaker with Microphone & Remote', 45.00, 25)"""
    se_item5 = """INSERT INTO small_electronics_items (name, description, price, quantity)
    VALUES ('3D Printer', 'XYZprinting da Vinci Mini Wireless 3D Printer-6"x6"x6" Volume ', 169.99, 25)"""


        ##populate toys table with data
    toys1 = """INSERT INTO toys (name, description, price, quantity)
    VALUES ('Teddy Bear', 'Joon Mini Teddy Bear, Tan, 13 Inches', 13.75, 25)"""
    toys2 = """INSERT INTO toys (name, description, price, quantity)
    VALUES ('Bicycle', 'Huffy 26" Cranbrook Mens Beach Cruiser Bike, Red Metallic', 95.00, 25)"""
    toys3 = """INSERT INTO toys (name, description, price, quantity)
    VALUES ('Remote Control Car', '27MHz 1/14 Scale Kids Licensed Ferrari Model Remote Control Toy Car w/ 5.1 MPH Max Speed, Red', 27.99, 25)"""
    toys4 = """INSERT INTO toys (name, description, price, quantity)
    VALUES ('Mini-trampoline', 'Stamina 36-Inch Trampoline Circuit Trainer with monitor', 42.00, 25)"""
    toys5 = """INSERT INTO toys (name, description, price, quantity)
    VALUES ('Blowup Pool', 'Intex Swim Center Family Inflatable Lounge Pool, 88" x 85" x 30"', 52.99, 25)"""

    #create database connection
    conn = create_connection(database)
    c = conn.cursor()

    #create table
    if conn is not None:
        create_table(conn, household_items_table)
        create_table(conn, books_table)
        create_table(conn, toys_table)
        create_table(conn, small_electronics_table)
    else:
        print("Error! Cannot create the table.")

        ##insert the data in to the household items table
    if conn is not None:
        insert_data(conn, household_item1)
        insert_data(conn, household_item2)
        insert_data(conn, household_item3)
        insert_data(conn, household_item4)
        insert_data(conn, household_item5)
    else:
        print("Failed to populate table with data.\n")

        ##insert the data in to the books table
    if conn is not None:
        insert_data(conn, books1)
        insert_data(conn, books2)
        insert_data(conn, books3)
        insert_data(conn, books4)
        insert_data(conn, books5)
    else:
        print("Failed to populate table with data.\n")

        ##insert the data in to the small electronics items table
    if conn is not None:
        insert_data(conn, se_item1)
        insert_data(conn, se_item2)
        insert_data(conn, se_item3)
        insert_data(conn, se_item4)
        insert_data(conn, se_item5)
    else:
        print("Failed to populate table with data.\n")

        ##insert the data in to toys table
    if conn is not None:
        insert_data(conn, toys1)
        insert_data(conn, toys2)
        insert_data(conn, toys3)
        insert_data(conn, toys4)
        insert_data(conn, toys5)
    else:
        print("Failed to populate table with data.\n")

#function to query a customer's item
def add_to_cart(conn, item_query, quantity_query, current_total, current_cart):
    try:
        c = conn.cursor()

        #get current item price from database
        c.execute("SELECT * FROM household_items WHERE name=:item", {"item":item_query})
        item_found = c.fetchone()
        if (item_found is not None):
            #check if there is enough inventory
            c.execute("SELECT quantity FROM household_items WHERE name=:item", {"item":item_query})
            item_quantity = c.fetchone()
            item_quantity = functools.reduce(lambda sub, ele: sub * 10 + ele, item_quantity)
            #update inventory
            if (item_quantity > 0):
                c.execute("UPDATE household_items SET quantity = quantity - 1 WHERE name=:item", {"item":item_query})
                conn.commit()
                #update current cart
                current_cart.append(item_found)
                c.execute("SELECT price FROM household_items WHERE name=:item", {"item":item_query})
                item_price = c.fetchone()
                res = functools.reduce(lambda sub, ele: sub * 10 + ele, item_price)
                print("Adding current total: ", current_total, "with item price", res)
                current_total += res



        #get current item price from database
        c.execute("SELECT * FROM books WHERE name=:item", {"item":item_query})
        item_found = c.fetchone()
        if (item_found is not None):
            #check if there is enough inventory
            c.execute("SELECT quantity FROM books WHERE name=:item", {"item":item_query})
            item_quantity = c.fetchone()
            item_quantity = functools.reduce(lambda sub, ele: sub * 10 + ele, item_quantity)
            #update inventory
            if (item_quantity > 0):
                c.execute("UPDATE books SET quantity = quantity - 1 WHERE name=:item", {"item":item_query})
                conn.commit()
                #update current cart
                current_cart.append(item_found)
                c.execute("SELECT price FROM books WHERE name=:item", {"item":item_query})
                item_price = c.fetchone()
                res = functools.reduce(lambda sub, ele: sub * 10 + ele, item_price)
                print("Adding current total: ", current_total, "with item price", res)
                current_total += res


        #get current item price from database
        c.execute("SELECT * FROM small_electronics_items WHERE name=:item", {"item":item_query})
        item_found = c.fetchone()
        if (item_found is not None):
            #check if there is enough inventory
            c.execute("SELECT quantity FROM small_electronics_items WHERE name=:item", {"item":item_query})
            item_quantity = c.fetchone()
            item_quantity = functools.reduce(lambda sub, ele: sub * 10 + ele, item_quantity)
            #update inventory
            if (item_quantity > 0):
                c.execute("UPDATE small_electronics_items SET quantity = quantity - 1 WHERE name=:item", {"item":item_query})
                conn.commit()
                #update cart
                current_cart.append(item_found)
                c.execute("SELECT price FROM small_electronics_items WHERE name=:item", {"item":item_query})
                item_price = c.fetchone()
                res = functools.reduce(lambda sub, ele: sub * 10 + ele, item_price)
                print("Adding current total: ", current_total, "with item price", res)
                current_total += res



        #get current item price from database
        c.execute("SELECT * FROM toys WHERE name=:item", {"item":item_query})
        item_found = c.fetchone()
        if (item_found is not None):
            #check if there is enough inventory
            c.execute("SELECT quantity FROM toys WHERE name=:item", {"item":item_query})
            item_quantity = c.fetchone()
            item_quantity = functools.reduce(lambda sub, ele: sub * 10 + ele, item_quantity)
            #update inventory
            if (item_quantity > 0):
                c.execute("UPDATE toys SET quantity = quantity - 1 WHERE name=:item", {"item":item_query})
                conn.commit()
                #update cart
                current_cart.append(item_found)
                c.execute("SELECT price FROM toys WHERE name=:item", {"item":item_query})
                item_price = c.fetchone()
                res = functools.reduce(lambda sub, ele: sub * 10 + ele, item_price)
                print("Adding current total: ", current_total, "with item price", res)
                current_total += res


        return current_total
    except Error as e:
        print(e)

#function to remove an item from the current cart
def remove_from_cart(conn, current_cart, remove_item, current_total):
    try:
        c = conn.cursor()
        #update cart
        updated_cart = [i for i in current_cart if i[0] != remove_item]
        print("Updated Cart: ", str(updated_cart))

        #update total price of cart
        k = 0;
        for k in current_cart:
            if (k[0] == remove_item):
                current_total -= k[2];

                #update quantities in database
                c.execute("UPDATE household_items SET quantity = quantity + 1 WHERE name=:item", {"item":remove_item})
                conn.commit()
                c.execute("UPDATE books SET quantity = quantity + 1 WHERE name=:item", {"item":remove_item})
                conn.commit()
                c.execute("UPDATE small_electronics_items SET quantity = quantity + 1 WHERE name=:item", {"item":remove_item})
                conn.commit()
                c.execute("UPDATE toys SET quantity = quantity + 1 WHERE name=:item", {"item":remove_item})
                conn.commit()
                #print("Item quantities updated.")

        return updated_cart, current_total
    except Error as e:
        print(e)


def main():
    #--------------------Uncomment next line to setup database--------------------
    #setup_database()

    database = (r"C:\sqlite\db\osc_system.db")

    #create database connection
    conn = create_connection(database)
    c = conn.cursor()

    #create running total of current cart
    total = 0
    #create current cart
    cart = []
    #track if a valid item was searched
    valid_search = True;

    #prompt user with shopping choices
    if conn is not None:

        checkout = False;
        while (checkout is not True):
            #display inventory to user
            display_inventory(conn)

            #prompt user to select items by category, name, and quantity
            user_item_choice = str(input("Enter the name of the item you would like to add to your current shopping cart: "))
            user_quantity_choice = int(input("Enter the quantity of the item you would like to purchase: "))

            while (user_quantity_choice <= 0):
                print("Please enter a valid quantity greater than 0.")
                user_quantity_choice = int(input("Enter the quantity of the item you would like to purchase: "))

            i = 0;
            for i in range(user_quantity_choice):
                temp = total
                #call function to add item to cart
                current_total = add_to_cart(conn,user_item_choice, user_quantity_choice, total, cart)
                total = current_total
                #check if valid item was entered
                if (total <= temp):
                    print("\nERROR: ITEM NOT FOUND. Please enter a valid item name and quantity from the listed inventory.")
                    valid_search = False;
                    break;
            #redisplay inventory after invalid item search
            if (valid_search == False):
                display_inventory(conn)

            print("Current Items in Cart: ", cart)
            print("Current Total: ", total)
            print("\n")
            user_answer = str(input("Would you like to checkout (c), remove an item (r), add an item (a), or view past purchases (p)?: "))
            print("\n")

            if (user_answer == "c"):
                checkout = True;
                print("Proceed to checkout.")
            if (user_answer == "r"):
                print("Remove an item was chosen.")
                item_to_remove = str(input("Enter the name of the item you would like to remove (all instances will be removed): "))
                remove_call = remove_from_cart(conn, cart, item_to_remove, total)
                cart = remove_call[0]
                total = remove_call[1]
                print(item_to_remove, " removed from your cart.")
                print("Current Items in Cart: ", cart)
                print("Current Total: ", total)
                print("\n")

            if (user_answer == "p"):
                history = True;
                print("View past transactions was chosen.")




main()
