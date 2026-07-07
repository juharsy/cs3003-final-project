CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    address TEXT
);

CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT
);

CREATE TABLE Product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity_in_stock INTEGER NOT NULL DEFAULT 0,
    staff_id INTEGER,
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

CREATE TABLE Purchase (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    staff_id INTEGER,
    quantity INTEGER NOT NULL DEFAULT 1,
    purchase_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

-- Sample data
INSERT INTO Staff (name, role) VALUES
('Alice Reyes', 'Inventory Manager'),
('Ben Chu', 'Sales Associate'),
('Carla Diaz', 'Store Manager');

INSERT INTO Customer (name, email, phone, address) VALUES
('John Smith', 'jsmith@email.com', '555-0101', '12 Oak St'),
('Maria Lopez', 'mlopez@email.com', '555-0102', '45 Pine Ave'),
('David Kim', 'dkim@email.com', '555-0103', '78 Maple Rd'),
('Emily Chen', 'echen@email.com', '555-0104', '90 Birch Ln'),
('Sam Patel', 'spatel@email.com', '555-0105', '33 Cedar Ct');

INSERT INTO Product (name, price, quantity_in_stock, staff_id) VALUES
('Wireless Mouse', 24.99, 50, 1),
('Mechanical Keyboard', 129.99, 30, 1),
('USB-C Hub', 39.50, 40, 2),
('27in Monitor', 249.99, 15, 2),
('Laptop Stand', 34.00, 25, 3);

INSERT INTO Purchase (customer_id, product_id, staff_id, quantity, purchase_date) VALUES
(1, 2, 2, 1, '2026-06-01'),
(2, 4, 3, 1, '2026-06-03'),
(3, 1, 1, 2, '2026-06-05'),
(4, 3, 2, 1, '2026-06-10'),
(5, 4, 3, 1, '2026-06-12'),
(1, 5, 3, 1, '2026-06-15');
