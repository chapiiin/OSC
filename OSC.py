import sqlite3
from sqlite3 import Error
from loginLogout import LoginView
from loginLogout import LogoutView
from DatabaseFile import DatabaseSystem
from SystemFile import System

#user login function
def Login(connection):
    account_exists = False;
    username = input("Please enter a valid username: ")
    password = input("Please enter a valid password: ")

    c = connection
    result = c.execute("SELECT username, password FROM user_accounts WHERE username=:name and password=:pass", {"name":username, "pass":password})
    rows = c.fetchall()
    for row in rows:
        account_exists = True;

    #query database for account
    if (account_exists == True):
        return username, password, True;
    return username, password, False;

#user logout function
def Logout():
    print("Successfully logged out.")
    return False;

def main():
    #Instaniate classes
    D = DatabaseSystem()
    S = System()

    #--------------------Uncomment next line to setup database-------------------
    D.setup_database()

    database = (r"C:\sqlite\db\osc_system.db")

    #create database connection
    conn = D.create_connection(database)
    c = conn.cursor()

    #Have the user login
    logged_in = False;

    while (logged_in == False):
        login_call = Login(c)
        logged_in = login_call[2]
        username = login_call[0]
        password = login_call[1]
        print("User logged in: ", logged_in)

    #create running total of current cart
    total = 0
    #create current cart
    cart = []
    #track if a valid item was searched
    valid_search = True;
    started_shopping = False;

    #prompt user with shopping choices
    if conn is not None:

        checkout = False;
        while (checkout is not True):
            if (started_shopping == False):
                user_query = str(input("Would you like to shop (s) or view past purchases (p)?: "))

            if (user_query == "s"):
                started_shopping = True;
                #display inventory to user
                S.display_inventory(conn)

                #prompt user to select items by category, name, and quantity
                user_item_choice = str(input("Enter the name of the item you would like to add to your current shopping cart: "))
                user_quantity_choice = input("Enter the quantity of the item you would like to purchase: ")

                #check if the user entered a valid quantity
                valid_digit = S.is_digit(user_quantity_choice)
                while (valid_digit is not True):
                    print("Please, enter a valid integer greater than 0.")
                    user_quantity_choice = input("Enter the quantity of the item you would like to purchase: ")
                    valid_digit = S.is_digit(user_quantity_choice)
                #ensure item quanitity is an integer
                user_quantity_choice = int(user_quantity_choice)

                while (user_quantity_choice <= 0):
                    print("Please enter a valid quantity greater than 0.")
                    user_quantity_choice = int(input("Enter the quantity of the item you would like to purchase: "))

                i = 0;
                for i in range(user_quantity_choice):
                    temp = total
                    #call function to add item to cart
                    current_total = S.add_to_cart(conn,user_item_choice, user_quantity_choice, total, cart)
                    total = current_total
                    #check if valid item was entered
                    if (total <= temp):
                        print("\nERROR: ITEM NOT FOUND. Please enter a valid item name and quantity from the listed inventory.")
                        valid_search = False;
                        break;
                #redisplay inventory after invalid item search
                if (valid_search == False):
                    S.display_inventory(conn)

                print("Current Items in Cart: ", cart)
                print("Current Total: ", total)
                print("\n")

            if(user_query == "p"):
                print("Past purchases was chosen.")
                S.transaction_history(username, c)
            if (started_shopping == True):

                user_answer = str(input("Would you like to checkout (c), remove an item (r), add an item (a), view past purchases (p), logout (l), or exit the program (e)?: "))
                print("\n")

                if (user_answer == "c"):
                    checkout = True;
                    S.user_checkout(conn, cart, total, username)

                if (user_answer == "r"):
                    print("Remove an item was chosen.")
                    item_to_remove = str(input("Enter the name of the item you would like to remove (all instances will be removed): "))
                    remove_call = S.remove_from_cart(conn, cart, item_to_remove, total)
                    cart = remove_call[0]
                    total = remove_call[1]
                    print(item_to_remove, " removed from your cart.")
                    print("Current Items in Cart: ", cart)
                    print("Current Total: ", total)
                    print("\n")

                if (user_answer == "p"):
                    print("View past transactions was chosen.")
                    S.transaction_history(username, c)

                if (user_answer == "l"):
                    logged_in = Logout()
                    exit()

                if (user_answer == "e"):
                    exit()




main()
