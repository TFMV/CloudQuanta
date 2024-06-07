import unittest
import pyarrow as pa
from src.load_data.load_data_duckdb import load_arrow_to_duckdb

class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        table = pa.table({'column1': [1, 2, 3]})
        conn = load_arrow_to_duckdb(table, 'test_table')
        result = conn.execute("SELECT * FROM test_table").fetchall()
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
