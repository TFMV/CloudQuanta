import unittest
from src.fetch_data.fetch_data_gcs import fetch_data_from_gcs

class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        bucket_name = 'your-bucket-name'
        source_blob_name = 'path/to/source/file.csv.gz'
        table = fetch_data_from_gcs(bucket_name, source_blob_name)
        self.assertIsNotNone(table)

if __name__ == '__main__':
    unittest.main()
