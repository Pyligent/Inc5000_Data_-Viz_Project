import os
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
engine = create_engine(SQLALCHEMY_DATABASE_URI)
#engine = create_engine('postgresql+psycopg2://postgres:postgres@@127.0.0.1/inc5000')

# 1. Load INC5000 2018 Data into the PostgreSQL Database

df = pd.read_csv('data/inc5000_2018.csv', sep=',').replace(to_replace='null', value=np.NaN)

df.columns = ['id', 'url', 'rank', 'city', 'ifmid', 'ifiid',
       'growth', 'workers', 'company', 'website','state_l', 'state_s', 'revenue', 'zipcode',
       'founded', 'industry', 'latitude', 'metrocode',
       'longitude', 'yrs_on_list', 'previous_workers', 'metro',
       'partner_lists']

df.to_sql('inc2018_data',  con=engine)

#2. Load INC5000 2007-2017 Data into the PostgreSQL Database

inc_ten_df = pd.read_csv('data/inc5000_all10years.csv', sep=',',encoding = 'unicode_escape').replace(to_replace='null', value=np.NaN)

inc_ten_df.columns = ['year', 'rank', 'city', 'growth', 'workers',
       'company', 'state_s', 'state_l', 'revenue',
       'yrs_on_list', 'industry', 'metro']

inc_ten_df.to_sql('inc2007_2017_data',  con=engine)

