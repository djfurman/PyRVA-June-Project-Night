import psycopg2
import pandas as pd


# establish connection to the database
conn = psycopg2.connect(
    dbname="can",
    user="python",
    password="pythonuser",
    host="pyrva.cul6zd3pcwrp.us-east-2.rds.amazonaws.com",
)

# create the query to pull the data
q = """
    SELECT *
    FROM google_play_data
"""

# the data is stored in the 'result' variable
df = pd.read_sql(q, conn)  # this is a pandas data frame

# print(df.count())  # Tells all column names and all of the columns in the data

de_duplicated = df['app_name'].unique()
print(len(de_duplicated))

# close the connection to the database
conn.close()
