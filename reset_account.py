import psycopg2
from psycopg2 import sql
from  war_clone_test import GenericDBHelper
# Define connection parameters
db_params = {
    'host': 'sthub.c3uguk04fjqb.ap-southeast-2.rds.amazonaws.com',
    'database': 'postgres',
    'user': 'stpostgres',
    'password': 'stocktrader'
}


# Establish the connection
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

q = '''UPDATE  war_iter_5.account
SET active_strength = 0,
    user_id = 1,
    total_strength = 50000,
    remaining_strength = 50000
    
WHERE account_id = 1;'''




cur.execute(q)
conn.commit()
print("done")
