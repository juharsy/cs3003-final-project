class Person:
    def __init__(self, person_id, name):
        self._id = person_id
        self._name = name

    @property
    def name(self):
        return self._name

    def display_info(self):
        return f"[Person] ID: {self._id}, Name: {self._name}"


class Customer(Person):
    def __init__(self, person_id, name, email, phone, address):
        super().__init__(person_id, name)
        self.email = email
        self.phone = phone
        self.address = address

    def display_info(self):
        return f"[Customer] ID: {self._id}, Name: {self._name}, Email: {self.email}"

    def view_purchase_history(self, conn):
        cur = conn.cursor()
        cur.execute("""
            SELECT Product.name, Purchase.quantity, Purchase.purchase_date
            FROM Purchase
            JOIN Product ON Purchase.product_id = Product.product_id
            WHERE Purchase.customer_id = ?
        """, (self._id,))
        return cur.fetchall()


class Staff(Person):
    def __init__(self, person_id, name, role):
        super().__init__(person_id, name)
        self.role = role

    def display_info(self):
        return f"[Staff] ID: {self._id}, Name: {self._name}, Role: {self.role}"

    def add_product(self, conn, name, price, stock):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Product (name, price, quantity_in_stock, staff_id) VALUES (?, ?, ?, ?)",
            (name, price, stock, self._id)
        )
        conn.commit()
        return cur.lastrowid

    def process_purchase(self, conn, customer_id, product_id, quantity):
        cur = conn.cursor()
        cur.execute("SELECT quantity_in_stock, price FROM Product WHERE product_id = ?", (product_id,))
        result = cur.fetchone()
        if not result:
            return None, "Product not found."
        stock, price = result
        if quantity > stock:
            return None, f"Not enough stock. Only {stock} available."

        from datetime import date
        today = date.today().isoformat()
        cur.execute(
            "INSERT INTO Purchase (customer_id, product_id, staff_id, quantity, purchase_date) VALUES (?, ?, ?, ?, ?)",
            (customer_id, product_id, self._id, quantity, today)
        )
        cur.execute(
            "UPDATE Product SET quantity_in_stock = quantity_in_stock - ? WHERE product_id = ?",
            (quantity, product_id)
        )
        conn.commit()
        return price * quantity, None


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self._price = price
        self.stock = stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def display_info(self):
        return f"[Product] {self.name} — ${self._price:.2f}, Stock: {self.stock}"
