from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    print('Starting NTC Taxi Data Pipeline...')

    raw_data = extract_data()
    clean_data = transform_data(raw_data)
    load_data(clean_data)

    print('Pipeline completed successfully.')

if __name__ == '__main__':
    main()