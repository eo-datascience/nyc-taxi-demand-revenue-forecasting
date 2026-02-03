import pandas as pd

def transform_data(data):
    print('Transforming data...')

    data = data.copy()

    #Convert datetime columns
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
    data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])

    #Remove invalid timestamps
    data = data[data['tpep_dropoff_datetime'] > data['tpep_pickup_datetime']]

    #Create trip duration feature
    data['trip_duration_min'] = (
        (data['tpep_dropoff_datetime'] - data['tpep_pickup_datetime'])
        .dt.total_seconds() / 60
    )

    #Remove unrealistic trips
    data = data[(data['trip_duration_min'] > 0) & (data['trip_duration_min'] < 600)]

    #Remove negative values
    data = data[(data['trip_distance'] >= 0) & (data['total_amount'] >= 0)]

    #Keep only 2022 Q1 data
    data = data[
        (data['tpep_pickup_datetime'] >= '2022-01-01') & (data['tpep_pickup_datetime'] < '2022-04-01')
    ]

    print(f'Transformed dataset shape: {data.shape}')
    return data

