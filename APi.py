import requests
from pandas import json_normalize
import pandas as pd
import psycopg2
from pymongo import MongoClient, errors

locationn = {
    'Kathmandu':[27.7172,85.3240],
    'Pokhara':[28.2096,83.9856],
    'Lalitpur':[27.6644,85.3188],
    'Biratnagar':[26.4525,87.2718],
    'Chitwan':[27.5291,84.3542],
    'Tokyo':[35.6895,139.6917],
    'NewYork':[40.7128,-74.0060],
    'Kyoto':[35.0116,135.7681],
    'Osaka':[34.6937,135.5023],
    'Bhaktapur':[27.6710,85.4298]
}

try:
    conn = psycopg2.connect(
        dbname = 'weather',
        user = 'postgres',
        password = '9849647940',
        host = 'localhost',
        port = '5433' 
    )
    print("Database connected successfully!")
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
    
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['weather_info']
    collection = db['Collection']
    print("Connection to MongoDB successful!")
except errors.ConnectionFailure as e:
    print("Could not connect to MongoDB:", e)

    
def extract():
    all_data = []
    api = '404a6671d9501ed93d41c8564830c02c'
    for city,(lat,lon) in locationn.items():
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'
        response = requests.get(url)
        data = response.json()
        all_data.append(data)
    print (data)
    collection.insert_many(all_data)
    print("INSERTION ON MONGO DB COMPLETE")
    return all_data


def transform(all_data):
    df = json_normalize(
        all_data,
        sep='_',
        record_path=['weather'],
        meta=[
            'base', 'visibility', 'dt', 'timezone',
            ['main', 'temp'], ['main', 'feels_like'], ['main', 'humidity'],
            ['wind', 'speed'], ['wind', 'deg'], ['wind', 'gust'],
            ['clouds', 'all'],
            ['sys', 'country'], ['sys', 'sunrise'], ['sys', 'sunset'],
            'id', 'name', 'cod'
        ],
        meta_prefix='meta_',
        errors='ignore',
    )
    df.set_index('meta_id', inplace=True)
    df['meta_sys_sunrise'] = pd.to_datetime(df['meta_sys_sunrise'],unit='s')
    df['meta_sys_sunset'] = pd.to_datetime(df['meta_sys_sunset'],unit='s')
    print(df)
    return df


def load(df, conn):
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (
                weather_id, main, description, icon, base, visibility, dt,
                timezone, temp, feels_like, humidity,
                wind_speed, wind_deg, wind_gust, clouds_all,
                country, sunrise, sunset, city_id, city_name, cod
            ) VALUES (%s, %s, %s, %s, %s, %s, to_timestamp(%s), %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['id'], row['main'], row['description'], row['icon'], row['meta_base'],
            row['meta_visibility'], row['meta_dt'], row['meta_timezone'],
            row['meta_main_temp'], row['meta_main_feels_like'], row['meta_main_humidity'],
            row['meta_wind_speed'], row['meta_wind_deg'], row.get('meta_wind_gust'),
            row['meta_clouds_all'], row['meta_sys_country'],
            row['meta_sys_sunrise'], row['meta_sys_sunset'],
            row.name, row['meta_name'], row['meta_cod']
        ))
    conn.commit()
    cursor.close()
    print("Data loaded into PostgreSQL successfully!")

    
    

all_data = extract()
df = transform(all_data)
load(df,conn)
