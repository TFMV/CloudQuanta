import pyarrow.csv as pv
import pyarrow.parquet as pq
import pyarrow as pa
import pyarrow.fs as fs
import os

def fetch_data_from_gcs(bucket_name, source_blob_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/thomasmcgeehan/CloudQuanta/CloudQuanta/sa.json"
    gcs_filesystem = fs.GcsFileSystem()
    gcs_path = f"{bucket_name}/{source_blob_name}"
    try:
        with gcs_filesystem.open_input_stream(gcs_path, compression="gzip") as file:
            if source_blob_name.endswith(".csv.gz"):
                arrow_table = pv.read_csv(file)
            elif source_blob_name.endswith(".parquet.snappy") or source_blob_name.endswith(".parquet"):
                arrow_table = pq.read_table(file)
            else:
                raise ValueError("Unsupported file type: must be .csv.gz or .parquet")
    except Exception as e:
        print(f"Error accessing GCS file: {e}")
        raise
    return arrow_table
