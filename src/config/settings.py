import os

class Config:
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'path/to/your/credentials.json')
    DBT_PROFILE = os.getenv('DBT_PROFILE', 'path/to/dbt/profiles.yml')
    BUCKET_NAME = os.getenv('BUCKET_NAME', 'your-bucket-name')
    SOURCE_BLOB_NAME = os.getenv('SOURCE_BLOB_NAME', 'path/to/source/file.csv.gz')
    TABLE_NAME = os.getenv('TABLE_NAME', 'your_table_name')
