-- Create table for raw sales data (from the original CSV)
CREATE TABLE IF NOT EXISTS raw_sales_data (
    invoice_id VARCHAR(255),
    branch VARCHAR(50),
    city VARCHAR(100),
    customer_type VARCHAR(50),
    gender VARCHAR(50),
    product_line VARCHAR(100),
    unit_price NUMERIC,
    quantity INTEGER,
    date DATE,
    time TIME,
    payment_method VARCHAR(50),
    total NUMERIC,
    tax NUMERIC
);

-- Create the table for transformed hourly sales data
CREATE TABLE IF NOT EXISTS hourly_sales (
    id SERIAL PRIMARY KEY,
    branch VARCHAR(50),
    hour INTEGER,
    total_sales NUMERIC
);

-- Create the table for transformed branch performance data
CREATE TABLE IF NOT EXISTS branch_sales (
    id SERIAL PRIMARY KEY,
    branch VARCHAR(50),
    total_sales NUMERIC
);

-- Create the table for product line performance
CREATE TABLE IF NOT EXISTS category_sales (
    id SERIAL PRIMARY KEY,
    product_line VARCHAR(100),
    total_sales NUMERIC
);
