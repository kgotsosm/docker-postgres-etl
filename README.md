# Docker ETL Pipeline for Supermarket Sales Data

This repository contains an ETL (Extract, Transform, Load) pipeline implemented using Docker, PostgreSQL, and Python. The pipeline processes a supermarket sales dataset from Kaggle and loads it into a PostgreSQL database.

<div style="display: flex; justify-content: space-around; gap: 10">
    <img src="/image/docker.svg" alt="Docker" width="100" />
    <img src="/image/python.svg" alt="Python" width="100" />
    <img src="/image/postgresql.svg" alt="PostgreSQL" width="100" />
</div>

## Prerequisites

- Docker
- Docker Compose
- Python 3.x (for local development, if needed)

## Getting Started

### Clone the Repository

```bash
git clone git@github.com:kgotsosm/docker-etl.git
cd docker-etl
```

### Set Up the Environment

1. Create a .env file in the root of the project with the following content, add in the values as needed:

*NEVER EXPOSE THIS FILE PUBLICLY*

DB_HOST<br>
DB_PORT<br>
DB_USER<br>
DB_PASSWORD<br>
DB_NAME<br>

### Build and Run the Services
 - Use Docker Compose to build and run the services:

```bash
docker-compose up --build
```

This will start both the PostgreSQL database and the ETL service. The ETL script will load the data into the database automatically.

### Accessing the Database

Once the ETL process completes, you can access the PostgreSQL database using a PostgreSQL client or through the command line:
```bash
psql -h your_host -U your_username -d sales_db
```


### Usage
After setting up, the ETL pipeline will:

- Extract data from data/supermarket_sales.csv
- Transform the data to generate insights such as hourly sales, branch performance, and category sales.
- Load the transformed data into the PostgreSQL database in the corresponding tables. There will be 4 tables (branch_sales, category_sales, hourly_sales and raw_sales_data)
