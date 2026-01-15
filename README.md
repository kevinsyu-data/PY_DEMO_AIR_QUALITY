# Air Quality Data Pipeline

An end-to-end data pipeline that extracts air quality data from OpenAQ API, processes it through AWS services, and loads it into Amazon Redshift for analytics

Project Overview

    This project demonstrates a production-ready data engineering pipeline that:
    - Ingests air quality data from OpenAQ API (>1000 global monitoring points)
    - Stores raw JSON data in AWS S3
    - Flattens nested JSON structure and store in AWS S3 using AWS Glue Visual ETL
    - Create structure by cataloging the data using AWS Glue Crawler 
    - Transact structured data using Amazon Redshift for BI and Analytics

Key Skills Demonstrated

    - ETL Pipeline Development
    - REST API Utilizaiton
    - AWS Data Services (S3, Glue, Redshift)
    - JSON Data Processing & Flattening
    - Data Cataloging & Schema Management
    - SQL Query Optimization
    - Python Development

Architecture

    OpenAQ API
        ↓
    Python Script (api_client.py)
        ↓
    AWS S3 (Raw JSON)
        ↓
    AWS Glue ETL Job (Flatten)
        ↓
    AWS S3 (Parquet)
        ↓
    AWS Glue Crawler (Catalog)
        ↓
    AWS Redshift Spectrum

Technologies Used

    - Languages: Python 3.9+
    - Cloud Platform: AWS
        - S3 for data lake storage
        - Glue for ETL and data cataloging
        - Redshift Serverless for data warehousing
        - IAM for security and permissions
    - Libraries: boto3, requests, pandas, dotenv
    - Data Format: JSON, JSON Lines, Parquet
    - API: OpenAQ REST API

Data Flow

    1. Data Ingestion (Python)
        - Fetch JSON from OpenAQ API
        - client.fetch_and_upload_to_s3(bucket_name)

    2. Data Transformation
        - Flattens nested JSON structures 
        - Extracts fields from objects
        - Converts arrays to queryable columns
        - Outputs optimized Parquet format

    3. Data Cataloging
        - AWS Glue Crawler automatically detects schema
        - Creates metadata in Glue Data Catalog
        - Enables querying via Redshift Spectrum

    4. Query S3 Directly (SQL)
        - One-time setup
            CREATE EXTERNAL SCHEMA air_quality_glue
            FROM DATA CATALOG
            DATABASE 'air_quality_db'
            IAM_ROLE 'arn:aws:iam::ACCOUNT:role/ROLE'
            REGION 'your region';
        - Sample Query
            SELECT * FROM air_quality.measurements LIMIT 10;

