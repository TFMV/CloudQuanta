import unittest
from unittest.mock import patch
from src.transform_data.run_dbt import run_dbt

class TestTransformData(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_dbt(self, mock_run):
        mock_run.return_value.returncode = 0
        run_dbt()
        mock_run.assert_called_with(["dbt", "run"], capture_output=True, text=True)

if __name__ == '__main__':
    unittest.main()
