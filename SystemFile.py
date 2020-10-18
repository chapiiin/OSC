import sqlite3
from sqlite3 import Error
import functools
from DatabaseFile import DatabaseSystem

class System:
    #function to display all current inventory items
    def display_inventory(self, conn):
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

    #function to query a customer's item
    def add_to_cart(self, conn, item_query, quantity_query, current_total, current_cart):
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
    def remove_from_cart(self, conn, current_cart, remove_item, current_total):
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

    #convert an array to a string
    def listToString(self, s):
        #initialize an empty string
        str1 = ' '.join([str(elem) for elem in s])
        return str1
    #function for a customer to checkout
    def user_checkout(self, conn, final_cart, final_price, user):
        #D = DatabaseSystem()
        c = conn.cursor()
        print("Proceeding to checkout.")
        print("\n")
        try:
            address = str(input("Please, provide a shipping address for your order: "))
        except Error as e:
            print(e)
        try:
            osc_card_number = int(input("Please, provide your unique ten digit OSC card number for payment: "))
        except Error as e:
            print(e)
        print("User purchasing items: ", user)
        print("Items being purchased: ", final_cart)
        print("Shipping items to: ", address)
        print("Amount Due: ", final_price)
        print("\n")
        try:
            confirm_purchase = str(input("Would you like to finalize your order? (y/n): "))
            if (confirm_purchase == "y"):

                        #update quantities in database
                finalized_transaction = [user, address, final_cart, final_price, osc_card_number]
                finalized_transaction = self.listToString(finalized_transaction)
                print("FINALIZED PURCHASE: ", finalized_transaction)
                print("Order Successfully Submitted! Here is a list of our updated inventory!")

                c.execute("UPDATE customer_transactions SET transaction_information=:transaction WHERE username=:name", {"transaction":finalized_transaction, "name":user})
                conn.commit()
                self.display_inventory(conn)
            else:
                print("Order was not successfully confirmed.")
        except Error as e:
            print(e)

    def is_digit(self, check_input):
        if check_input.isdigit():
            return True
        return False

    #function to view past purchases
    def transaction_history(self, username, connection):
        print("Transaction History for", username)
        c = connection
        result = c.execute("SELECT transaction_information FROM customer_transactions WHERE username=:name", {"name":username})
        rows = c.fetchall()
        for row in rows:
            print(row)
