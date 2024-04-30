## Technologies
- Django
- Postgres
- Elasticsearch
- Kibana
- Docker

## Usage
Run:
> docker compose up --build

## API Documentation 
You can use a data search using (in all fields by prefix)
> http://127.0.0.1:8000/api/heritage_lost_objects-search?search= \
You can use search for multiple terms
> http://127.0.0.1:8000/api/heritage_lost_objects-search?search=query_1&search=query_2  
Search for multiple terms in specific fields
> http://127.0.0.1:8000/api/heritage_lost_objects-search?search=name:query_1&search=category:query_2  
Limit and offset:
> http://127.0.0.1:8000/api/heritage_lost_objects-search?search=name:query_1&search=category:query_2&limit=100&offset=0  
Default limit=10
# Filtering
Filter fields:
date_reg (registration date)
reg_number (registration number)
name
classification
category
state
height
width
length
weight

# Supported lookups
term

Find documents which contain the exact term specified in the field specified.

http://127.0.0.1:8000/api/heritage_lost_objects-search?name__term=картина&classification__term=красная

range

Find documents where the field specified contains values (dates, numbers, or strings) in the range specified.

From, to

http://127.0.0.1:8000/api/heritage_lost_objects-search?limit=100&date_reg__range=2021-04-21__2021-04-28
From, to, boost

exists

Find documents where the field specified contains any non-null value.

http://127.0.0.1:8000/api/heritage_lost_objects-search?width__exists=true

prefix

Find documents where the field specified contains terms which begin with the exact prefix specified.

http://127.0.0.1:8000/api/heritage_lost_objects-search?name__prefix=карт


## Ход моих мыслей при выполнении работы можно посмотреть по адресу:
https://docs.google.com/document/d/1cu-rqdk4s5yTDeIozu1gnlq7S07uanIgAxU26Z6O3gU




