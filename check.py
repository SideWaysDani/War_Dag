import psycopg2
from psycopg2 import sql
from war_clone_test import GenericDBHelper
# Define connection parameters
db_params = {
    'host': 'sthub.c3uguk04fjqb.ap-southeast-2.rds.amazonaws.com',
    'database': 'postgres',
    'user': 'stpostgres',
    'password': 'stocktrader'
}

# schema_name_global = "war_clone_test"
# Establish the connection
conn = psycopg2.connect(**db_params)
db_helper = GenericDBHelper(conn)
threshold_perc_for_unassigning = 4
# poor_performer_allocations = db_helper.select_all(
#         table_name='allocation',
#         columns='*',
#         where_clause=f"closing_price < opening_price-{threshold_perc_for_unassigning/100}"
#     )

# Create a cursor object
cur = conn.cursor()
start_date = '2024-05-15'
end_date = '2024-06-15'


# # Execute a simple SQL query
# # query = "SELECT * FROM stocktrader.stocks_leads WHERE start_date = %s"
# # query = "SELECT * FROM  war_clone_test.account"
global_schema_name = "war_iter_5"

query = f"UPDATE  {global_schema_name}.unit_assignment SET assignment_status = 'unassigned'"
cur.execute(query)
conn.commit()


query = f"delete from  {global_schema_name}.allocation "
cur.execute(query)
conn.commit()
query = f"delete from  {global_schema_name}.deployment "
cur.execute(query)
conn.commit()
query = f"delete from  {global_schema_name}.deployment_history "
cur.execute(query)
conn.commit()
query = f"delete from  {global_schema_name}.performance "
cur.execute(query)
conn.commit()
# query = f"delete from  {global_schema_name}.leads "
# cur.execute(query)
# conn.commit()
query = f"delete from  {global_schema_name}.allocation_history"
cur.execute(query)
conn.commit()
query = f"delete from  {global_schema_name}.account_history"
cur.execute(query)
conn.commit()
query = f"delete from  {global_schema_name}.summary"
cur.execute(query)
conn.commit()

print("result--------------------------start", global_schema_name)


# add_column_query = sql.SQL("""
#             ALTER TABLE  war_clone_test.allocation_history
#             ADD COLUMN battle_date date
#         """)

# # # Execute the SQL command
# cur.execute(add_column_query)

# # # Commit the changes
# conn.commit()

# print("Column 'deploy_id' of type 'INT' added to table 'depl_history'.")

# query = "delete from  war_clone_test.leads"
# cur.execute(query )
# conn.commit()


# query = "SELECT * FROM  war_clone_test.leads WHERE lead_date = %s "
# cur.execute(query )
# conn.commit()
# Fetch the result
# result = cur.fetchall()
# for r in results:
#     print(r[])
# import pandas as pd
# from polygon import RESTClient
# # print(result)

# client = RESTClient("x2WHlSdeMaaSJLsYgck_sVSdMFSAaNpu")
# dataRequest = client.get_aggs(ticker="WST",
#                               multiplier=1,
#                               timespan='day',
#                               from_="2024-06-17",
#                               to="2024-06-20")
# priceData = pd.DataFrame(dataRequest)
# print('------------', priceData)
# print('-----------------')
# if not priceData.empty:
#     priceData['Stock name'] = "WST"
#     priceData['Date'] = priceData['timestamp'].apply(
#         lambda x: pd.to_datetime(x*1000000))

#     priceData['Date'] = pd.to_datetime(
#         priceData['timestamp'] * 1000000).dt.strftime('%Y-%m-%d')

#     print(priceData)