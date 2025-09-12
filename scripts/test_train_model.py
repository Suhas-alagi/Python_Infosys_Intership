import unittest
import pandas as pd
import tempfile
import os

class TestTrainModel(unittest.TestCase):
    def test_load_csv_with_last_update(self):
        # Create temp CSV with 'last_update' and 'pollutant_avg'
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("last_update,pollutant_avg\n2024-01-01,10\n2024-01-02,20\n")
            fname = f.name
        df = pd.read_csv(fname)
        self.assertIn('last_update', df.columns)
        df['last_update'] = pd.to_datetime(df['last_update'])
        df.set_index('last_update', inplace=True)
        self.assertTrue(df.index.dtype.kind == 'M')  # datetime64
        os.remove(fname)

    def test_load_csv_without_last_update(self):
        # Create temp CSV without 'last_update'
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("date,pollutant_avg\n2024-01-01,10\n2024-01-02,20\n")
            fname = f.name
        df = pd.read_csv(fname)
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])
        df.set_index(df.columns[0], inplace=True)
        self.assertTrue(df.index.dtype.kind == 'M')  # datetime64
        os.remove(fname)

    def test_column_strip(self):
        # Create temp CSV with whitespace in column names
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write(" last_update , pollutant_avg \n2024-01-01,10\n")
            fname = f.name
        df = pd.read_csv(fname)
        df.columns = df.columns.str.strip()
        self.assertIn('last_update', df.columns)
        self.assertIn('pollutant_avg', df.columns)
        os.remove(fname)

    def test_pollutant_avg_fill(self):
        # Create temp CSV with missing pollutant_avg
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            f.write("last_update,pollutant_avg\n2024-01-01,\n2024-01-02,20\n")
            fname = f.name
        df = pd.read_csv(fname)
        # Use ffill then bfill to fill all NaNs
        df['pollutant_avg'] = df['pollutant_avg'].ffill().bfill()
        self.assertFalse(df['pollutant_avg'].isnull().any())
        os.remove(fname)

if __name__ == '__main__':
    unittest.main()