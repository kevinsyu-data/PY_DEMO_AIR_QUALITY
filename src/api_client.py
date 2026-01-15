import sys
from pathlib import Path

# Add the py_demo_air_quality directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

import requests
import json
import boto3
from datetime import datetime
from config import BASE_URL, API_KEY, S3_BUCKET_NAME

HEADERS = {'X-API-Key': API_KEY}

class OpenAQClient:
    def __init__(self):
        self.measurements_url = BASE_URL
        self.s3_client = boto3.client('s3')

    def fetch_data(self, limit=1000):
        params = {'limit': limit}
        response = requests.get(self.measurements_url, params=params, headers=HEADERS)
        print('Status Code:', response.status_code)
        
        data = response.json()
        records = data.get('results', [data])
        print(f'Fetched {len(records)} records')
        
        return data
    
    def upload_to_s3(self, data, bucket_name):
        
        # Extract and convert to JSON Lines format
        records = data.get('results', [data])
        jsonl_content = '\n'.join([json.dumps(records) for record in records])
        
        # Create filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        s3_key = f'air_quality/raw/{timestamp}.jsonl'
        
        # Upload to S3
        self.s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=jsonl_content.encode('utf-8')
        )
        
        print(f'Uploaded to s3://{bucket_name}/{s3_key}')
        
        return s3_key
    
    def fetch_and_upload_to_s3(self, bucket_name, limit=1000):
        data = self.fetch_data(limit)
        s3_key = self.upload_to_s3(data, bucket_name)
        
        return s3_key


if __name__ == "__main__":
    client = OpenAQClient()
    client.fetch_and_upload_to_s3(S3_BUCKET_NAME)