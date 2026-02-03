import duckdb

DB_PATH = '../warehouse/nyc_taxi.duckdb'

conn = duckdb.connect(DB_PATH)

schema = conn.execute('SELECT * FROM daily_taxi_metrics').df()
print(schema)

"""
def run_checks():
    print("Running data quality checks...")

    conn = duckdb.connect(DB_PATH)

    # Check table exists
    tables = conn.execute("SHOW TABLES").fetchall()
    print("Tables:", tables)

    # Row count
    row_count = conn.execute(
        "SELECT COUNT(*) FROM NYC_Taxi_Clean"
    ).fetchone()[0]

    print(f"Total rows in warehouse: {row_count:,}")

    # Sample rows
    sample = conn.execute(
        "SELECT * FROM NYC_Taxi_Clean LIMIT 5"
    ).df()

    print("\nSample data:")
    print(sample)

    conn.close()
    print("\nData quality checks passed.")

if __name__ == "__main__":
    run_checks()
"""