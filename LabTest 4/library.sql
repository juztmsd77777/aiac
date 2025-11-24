-- 🛒 E-COMMERCE PRODUCT INVENTORY SCHEMA (CLEAN VERSION)

-- 0️⃣ Drop existing tables if they already exist (to avoid duplicate errors)
DROP TABLE IF EXISTS Stock;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;

-- 1️⃣ Create Table: Suppliers
CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(255)
);

-- 2️⃣ Create Table: Products
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- 3️⃣ Create Table: Stock
CREATE TABLE Stock (
    stock_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT CHECK (quantity >= 0),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- 4️⃣ Insert Sample Data into Suppliers
INSERT INTO Suppliers (supplier_name, contact_email, phone_number, address) VALUES
('TechWorld Pvt Ltd', 'contact@techworld.com', '9876543210', 'Bangalore, India'),
('SmartSupplies Inc', 'sales@smartsupplies.com', '9123456780', 'Mumbai, India'),
('UrbanCart Ltd', 'info@urbancart.com', '9988776655', 'Delhi, India');

-- 5️⃣ Insert Sample Data into Products
INSERT INTO Products (product_name, category, price, supplier_id) VALUES
('Wireless Mouse', 'Electronics', 899.00, 1),
('Bluetooth Speaker', 'Electronics', 1499.00, 1),
('Office Chair', 'Furniture', 3599.00, 2),
('Water Bottle', 'Home Essentials', 299.00, 3),
('Desk Lamp', 'Home Essentials', 799.00, 3);

-- 6️⃣ Insert Sample Data into Stock
INSERT INTO Stock (product_id, quantity) VALUES
(1, 25),
(2, 8),
(3, 4),
(4, 12),
(5, 6);

-- 7️⃣ Query: Find Products with Stock Quantity Less Than 10
SELECT 
    p.product_name,
    p.category,
    s.quantity,
    sup.supplier_name
FROM 
    Products p
JOIN 
    Stock s ON p.product_id = s.product_id
JOIN 
    Suppliers sup ON p.supplier_id = sup.supplier_id
WHERE 
    s.quantity < 10;
SELECT 
    p.product_name,
    p.category,
    s.quantity,
    sup.supplier_name
FROM 
    Products p
JOIN 
    Stock s ON p.product_id = s.product_id
JOIN 
    Suppliers sup ON p.supplier_id = sup.supplier_id
WHERE 
    s.quantity < 10;
SELECT 
    p.product_name,
    p.category,
    s.quantity,
    sup.supplier_name
FROM 
    Products p
JOIN 
    Stock s ON p.product_id = s.product_id
JOIN 
    Suppliers sup ON p.supplier_id = sup.supplier_id
WHERE 
    s.quantity < 10;
