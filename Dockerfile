FROM python:3.9-slim

# Install dependencies
RUN pip install pandas sqlalchemy psycopg2-binary python-dotenv

WORKDIR /app

# Copy the ETL script and any required files
COPY etl_script.py /app/
COPY data/supermarket_sales.csv /app/data/

# Run the ETL script
CMD ["python", "etl_script.py"]
