import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pymysql

# database engine
engine = create_engine("mysql+pymysql://root:admin@localhost:3306/exercise_db")

# import csv file and convert to dataframe
df = pd.read_csv("exercise_database.csv")

#set index to 1 from 0
df.index = df.index + 1

# rename index column to id
df.index.name = 'id'

print(df)

# import dataframe into database
df.to_sql(con=engine, name="exercise", if_exists="replace")
