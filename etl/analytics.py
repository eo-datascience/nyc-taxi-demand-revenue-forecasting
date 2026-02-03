import duckdb

def run_analytics(db_path="../warehouse/nyc_taxi.duckdb"):
    conn = duckdb.connect(db_path)

    with open("../analytics/metrics.sql") as f:
        sql = f.read()

    conn.execute(sql)

    print("Analytics tables created successfully.")

    conn.close()

if __name__ == "__main__":
    run_analytics()