import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def extract():
    """Extract data from source (CSV) """
    try:
        data = pd.read_csv('data/supermarket_sales.csv')
        logging.info("Data extracted successfully.")
        return data
    except Exception as e:
        logging.error("Error during extraction: %s", e)
        raise

def transform(data):
    """Transform the data to get insights into the hourly sales, branch performance, and product line performance"""
    try:
        # Clean data
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Add hourly sales by extracting the hour from the time column
        data['Hour'] = pd.to_datetime(data['Time']).dt.hour
        hourly_sales = data.groupby(['Branch', 'Hour'])['Total'].sum().reset_index()

        # Analyze branch performance
        branch_sales = data.groupby('Branch')['Total'].sum().reset_index()
        
        # Category-level performance
        category_sales = data.groupby('Product line')['Total'].sum().reset_index()

        logging.info("Data transformed successfully.")
        return hourly_sales, branch_sales, category_sales
    except Exception as e:
        logging.error("Error during transformation: %s", e)
        raise

def load(hourly_sales, branch_sales, category_sales):
    """Load data into PostgreSQL"""
    try:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        
        # Load data into respective tables
        hourly_sales.to_sql('hourly_sales', engine, if_exists='replace', index=False)
        branch_sales.to_sql('branch_sales', engine, if_exists='replace', index=False)
        category_sales.to_sql('category_sales', engine, if_exists='replace', index=False)

        logging.info("Data loaded successfully into PostgreSQL.")
    except Exception as e:
        logging.error("Error during loading: %s", e)
        raise

if __name__ == '__main__':
    try:
        data = extract()
        hourly_sales, branch_sales, category_sales = transform(data)
        load(hourly_sales, branch_sales, category_sales)
    except Exception as e:
        logging.critical("ETL process failed: %s", e)
