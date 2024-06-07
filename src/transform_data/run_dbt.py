import subprocess
import os

def run_dbt(dbt_db_path):
    dbt_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dbt_project'))
    print(f"Expected dbt directory: {dbt_dir}")
    print(f"Contents of dbt directory: {os.listdir(dbt_dir)}")
    
    dbt_env = os.environ.copy()
    dbt_env["DBT_DUCKDB_PATH"] = dbt_db_path
    
    result = subprocess.run(["dbt", "run"], cwd=dbt_dir, capture_output=True, text=True, env=dbt_env)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise Exception("dbt run failed")
