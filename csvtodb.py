import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text, String, DateTime
import pymysql

# database engine
engine = create_engine("DATABASE_URL")

# import csv file and convert to dataframe
df = pd.read_csv("exercise_database.csv")

# import dataframe into database
df.to_sql(con=engine, name="exercises", if_exists="replace")
