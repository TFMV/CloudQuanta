import duckdb
import pyarrow as pa

def load_arrow_to_duckdb(arrow_table, table_name):
    schema_name, table_name = table_name.split('.')
    db_path = '/Users/thomasmcgeehan/CloudQuanta/CloudQuanta/dbt_project/dbt_duckdb.db'
    conn = duckdb.connect(database=db_path)
    conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
    conn.register("arrow_table", arrow_table)
    conn.execute(f"CREATE OR REPLACE TABLE {schema_name}.{table_name} AS SELECT * FROM arrow_table")
    print(f"Loaded data into DuckDB table: {schema_name}.{table_name}")

    # Verify the table creation
    result = conn.execute(f"SELECT * FROM {schema_name}.{table_name} LIMIT 1").fetchall()
    print(f"Verification result: {result}")
    
    return db_path
