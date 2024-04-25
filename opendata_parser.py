import requests
import threading
import psycopg2
from dotenv import load_dotenv
import os
import re

headers = {
    'X-API-KEY': '4065b6ccfb993ab5243f42be4cbbf0728721d71610a92ff9804981645cffe5f3'
}

url_count = f'https://opendata.mkrf.ru/v2/heritage_lost_objects/$?s=0&l=1'
response_count = requests.get(url_count, headers=headers)
count = response_count.json()['total']

load_dotenv()
conn = psycopg2.connect(
    dbname=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT')
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS heritage_lost_objects (
        id SERIAL PRIMARY KEY,
        date_reg DATE NOT NULL,
        reg_number INT,
        name VARCHAR,
        classification VARCHAR,
        category VARCHAR,
        state VARCHAR,
        height VARCHAR,
        width VARCHAR,
        length VARCHAR,
        weight VARCHAR
        )
""")


def get_value(obj, key):
    try:
        value = obj.get(key)
        if value != "":
            return value
        else:
            return None
    except KeyError:
        return None


def fetch_data(url):
    response = requests.get(url, headers=headers)
    data = response.json()['data']
    for obj in data:
        date_reg = get_value(obj['data']['general'], 'registrationDate')
        reg_number = get_value(obj['data']['general'], 'registerNumber')
        name = get_value(obj['data']['general'], 'name')
        classification = get_value(obj['data']['general']['classificationCulturalValue'], 'name') \
            if 'classificationCulturalValue' in obj['data']['general'] else None
        category = get_value(obj['data']['general']['categoryLostValue'], 'name') \
            if 'categoryLostValue' in obj['data']['general'] else None
        state = get_value(obj['data']['general'], 'conservationState')
        height = get_value(obj['data']['general'], 'height')
        width = get_value(obj['data']['general'], 'width')
        length = get_value(obj['data']['general'], 'length')
        weight = get_value(obj['data']['general'], 'weight')
        cur.execute('''
                INSERT INTO heritage_lost_objects (date_reg, reg_number, name, classification, category, state, height, width, length, weight)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                ''', (date_reg, reg_number, name, classification, category, state, height, width, length, weight))


def get_objects():
    threads = []
    for offset in range(0, count, 1000):
        url = f'https://opendata.mkrf.ru/v2/heritage_lost_objects/$?s={offset}&l=1000'
        thread = threading.Thread(target=fetch_data, args=(url, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return True


get_objects()

conn.commit()
