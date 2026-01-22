import psycopg2
import pandas as pd
from sklearn.linear_model import LinearRegression
conn = psycopg2.connect(
    dbname="bsdb",
    user="user",
    password="password",
    host="localhost",
    port="5432"
)


query = "SELECT temperature, city FROM weather_data;"
df = pd.read_sql(query, conn)

conn.close()

print(df.head())
print(df.columns)