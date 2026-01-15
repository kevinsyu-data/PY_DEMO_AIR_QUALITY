import os
from dotenv import load_dotenv

#Air Quality API Credentials and URL
BASE_URL = 'https://api.openaq.org/v3/locations'
API_KEY = os.getenv('API_KEY')

# AWS Credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')

#S3 Bucket
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
S3_RAW_PREFIX = 'air_quality/raw/'
S3_FLATTEN_PREFIX = 'air_quality/flatten/'

#Redshift Serverless Config
REDSHIFT_WORKGROUP = os.getenv('REDSHIFT_WORKGROUP')
REDSHIFT_DATABASE = os.getenv('REDSHIFT_DATABASE')
REDSHIFT_SCHEMA = os.getenv('REDSHIFT_SCHEMA')
REDSHIFT_IAM_ROLE = os.getenv('REDSHIFT_IAM_ROLE')

#Glue Configuration
GLUE_DATABASE = os.getenv('GLUE_DATABASE', 'air_quality_db')
GLUE_ROLE_ARN = os.getenv('GLUE_ROLE_ARN')
GLUE_CRAWLER_RAW = 'air-quality-raw-crawler'
GLUE_CRAWLER_FLATTEN = 'air-quality-flatten-crawler'

## API Configuration
API_REQUEST_TIMEOUT = 30
API_MAX_RETRIES = 3
API_RECORDS_LIMIT = 1000

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'