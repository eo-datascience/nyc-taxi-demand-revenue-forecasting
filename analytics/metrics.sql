-- Daily taxi performance metrics

CREATE OR REPLACE TABLE daily_taxi_metrics AS
SELECT
    DATE(tpep_pickup_datetime) AS trip_date,

    COUNT(*) AS total_trips,

    ROUND(AVG(trip_distance), 2) AS avg_trip_distance,

    ROUND(AVG(trip_duration_min), 2) AS avg_trip_duration_min,

    ROUND(AVG(total_amount), 2) AS avg_fare,

    ROUND(SUM(total_amount), 2) AS total_revenue

FROM NYC_Taxi_Clean
GROUP BY 1
ORDER BY 1;