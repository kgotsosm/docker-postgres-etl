import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def extract():
    """Extract data from source (CSV) """
    data = pd.read_csv('data/supermarket_sales.csv')
    return data

def transform(data):
    """Transform the data to get insights into the hourly sales, branch performance and Produc line performance"""
    # Clean data
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Add hourly sales by extracting the hour from the time column
    data['Hour'] = pd.to_datetime(data['Time']).dt.hour
    hourly_sales = data.groupby(['Branch', 'Hour'])['Total'].sum().reset_index()

    # Analyze branch performance
    branch_sales = data.groupby('Branch')['Total'].sum().reset_index()
    
    # Category-level performance
    category_sales = data.groupby('Product line')['Total'].sum().reset_index()
    
    return hourly_sales, branch_sales, category_sales

def load(hourly_sales, branch_sales, category_sales):

    """Load data into PostgreSQL"""
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    data.to_sql('raw_sales_data', engine, if_exists='replace', index=False)
    
    hourly_sales.to_sql('hourly_sales', engine, if_exists='replace', index=False)
    branch_sales.to_sql('branch_sales', engine, if_exists='replace', index=False)
    category_sales.to_sql('category_sales', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    data = extract()
    hourly_sales, branch_sales, category_sales = transform(data)
    load(hourly_sales, branch_sales, category_sales)
