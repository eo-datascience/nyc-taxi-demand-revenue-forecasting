import duckdb
from pathlib import Path

def load_data(data, db_path='../warehouse/NYC_Taxi.duckdb'):
    """
    Loads cleaned data into DuckDB warehouse.
    """
    print('Loading data into DuckDB warehouse...')

    #Ensure warehouse directory exists
    Path('../warehouse').mkdir(exist_ok=True)

    #Connect to DuckDB
    conn = duckdb.connect(db_path)

    #Register dataframe ad DuckDB table
    conn.register('Taxi_data', data)

    #Create or replace main analytics table
    conn.execute("""
        CREATE OR REPLACE TABLE NYC_Taxi_Clean AS SELECT * FROM Taxi_data
    """)

    conn.close()

    print('Data successfully loaded into warehouse.')