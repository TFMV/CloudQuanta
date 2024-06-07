import sys
import os

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fetch_data.fetch_data_gcs import fetch_data_from_gcs
from src.load_data.load_data_duckdb import load_arrow_to_duckdb
from src.transform_data.run_dbt import run_dbt

def run_pipeline(bucket_name, source_blob_name, table_name):
    arrow_table = fetch_data_from_gcs(bucket_name, source_blob_name)
    db_path = load_arrow_to_duckdb(arrow_table, table_name)
    run_dbt(db_path)

if __name__ == "__main__":
    bucket_name = 'tfmv-fuse'
    source_blob_name = 'nation.csv.gz'
    table_name = 'tpch_copy.nation'
    run_pipeline(bucket_name, source_blob_name, table_name)
