import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path('../data/raw')

def extract_data():
    print('Extracting raw data...')

    files = list(RAW_DATA_DIR.glob('*parquet'))
    print(f'Found {len(files)} raw files')

    if not files:
        raise FileNotFoundError('No parquet files found in data/raw')
    
    data_list = [pd.read_parquet(file) for file in files]
    data = pd.concat(data_list, ignore_index=True)

    print(f'Combined dataset shape: {data.shape}')
    return data

