#!/usr/bin/env python
# coding: utf-8

# Connecting to Postgres with Jupyter and pgcli

import pandas as pd

pd.__version__

df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)

df

# Type of Datatype

pd.to_datetime(df.tpep_pickup_datetime)

# Change of DataType

df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)

from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5431/ny_taxi')

engine.connect()

pd.io.sql.get_schema(df,name='yellow_taxi_data')

print(pd.io.sql.get_schema(df,name='yellow_taxi_data', con=engine))


df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)

df_iter

df = next(df_iter)

len(df)

df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)

df

df.head(n=0)

df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# Loading of the first (100,000) chunk data

%time, df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

from time import time
while True:
    t_start = time()
    df = next(df_iter)
    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    t_end = time()
    print('inserted another chunk, took %.3f second' % (t_end - t_start))


