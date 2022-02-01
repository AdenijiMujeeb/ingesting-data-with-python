#!/usr/bin/env python
# coding: utf-8

# Connecting to Postgres with Jupyter and Pandas

# Keep postgres and jupyter running on different terminal

import pandas  as pd
````
pip install sqlalchemy  psycopg2-binary
```


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5431/ny_taxi')
engine.connect()

query="""
SELECT 1 as number 
""""

pd.read_sql(query, con=engine)

query="""
SELECT *
FROM pg_catalog.pg_tables
WHERE  schemaname !='pg_catalog' AND  schemaname!='information_schema'; 
""""
pd.read_sql(query, con=engine)

df=pd.read_csv('yellow_taxi_data', nrows=100)

df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)

df.to_sql(name='yellow_taxi_data', con=engine, index=False)

query="""
SELECT * FROM yellow_trip_data LIMIT 10
""""



