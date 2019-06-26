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
result = pd.read_sql(q, conn)

print(result.head(10))

# close the connection to the database
conn.close()
