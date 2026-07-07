import sqlite3
from models import Customer, Staff, Product

DB_FILE = "ecommerce.db"

def connect():
    return sqlite3.connect(DB_FILE)

def load_staff(conn, staff_id):
    cur = conn.cursor()
    cur.execute("SELECT staff_id, name, role FROM Staff WHERE staff_id = ?", (staff_id,))
    row = cur.fetchone()
    return Staff(*row) if row else None

def load_customer(conn, customer_id):
    cur = conn.cursor()
    cur.execute("SELECT customer_id, name, email, phone, address FROM Customer WHERE customer_id = ?", (customer_id,))
    row = cur.fetchone()
    return Customer(*row) if row else None

def view_products(conn):
    cur = conn.cursor()
    cur.execute("SELECT product_id, name, price, quantity_in_stock FROM Product")
    for row in cur.fetchall():
        print(Product(*row).display_info())

def add_product(conn):
    staff_id = int(input("Staff ID: "))
    staff = load_staff(conn, staff_id)
    if not staff:
        print("Staff not found.")
        return
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    new_id = staff.add_product(conn, name, price, stock)
    print(f"{staff.display_info()} added product ID {new_id}.")

def make_purchase(conn):
    staff_id = int(input("Staff ID (processing): "))
    staff = load_staff(conn, staff_id)
    if not staff:
        print("Staff not found.")
        return
    customer_id = int(input("Customer ID: "))
    product_id = int(input("Product ID: "))
    quantity = int(input("Quantity: "))
    total, error = staff.process_purchase(conn, customer_id, product_id, quantity)
    if error:
        print(error)
    else:
        print(f"Purchase processed by {staff.display_info()}. Total: ${total:.2f}")

def view_customer_history(conn):
    customer_id = int(input("Customer ID: "))
    customer = load_customer(conn, customer_id)
    if not customer:
        print("Customer not found.")
        return
    print(customer.display_info())
    rows = customer.view_purchase_history(conn)
    if not rows:
        print("No purchases found.")
    for r in rows:
        print(f"  {r[0]} | Qty: {r[1]} | Date: {r[2]}")

def main():
    conn = connect()
    while True:
        print("\n=== OOP E-Commerce CLI ===")
        print("1. View products")
        print("2. Add product (staff)")
        print("3. Make a purchase (staff)")
        print("4. View customer purchase history")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_products(conn)
        elif choice == "2":
            add_product(conn)
        elif choice == "3":
            make_purchase(conn)
        elif choice == "4":
            view_customer_history(conn)
        elif choice == "5":
            break
        else:
            print("Invalid option.")
    conn.close()

if __name__ == "__main__":
    main()
