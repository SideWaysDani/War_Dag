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

# Establish the connection
conn = psycopg2.connect(**db_params)
cur = conn.cursor()
db_helper = GenericDBHelper(conn)

# Schema name
global_schema_name = "war_iter_4_3"

# Reset account table
account_update_query = f"""
    UPDATE {global_schema_name}.account
    SET active_strength = 0,
        total_strength = 50000    ,
        remaining_strength = 50000    ,
        reserved_strength = 0
"""
cur.execute(account_update_query)
conn.commit()

# Update unit assignment
cur.execute(f"UPDATE {global_schema_name}.unit_assignment SET assignment_status = 'unassigned'")
conn.commit()

# Tables to clear
tables_to_delete_from = [
    "allocation", "deployment", "deployment_history",
    "performance", "allocation_history", "account_history", "summary"
]

# Delete data from multiple tables
for table in tables_to_delete_from:
    cur.execute(f"DELETE FROM {global_schema_name}.{table}")
    conn.commit()

print(f"Cleanup completed for schema: {global_schema_name}")


# just run warvenv to run this code
# echo 'alias warvenv="cd \"/media/sidewaysdani/Windows-SSD/Users/Daiynal Asim/Downloads/War_Dags\" && source venv/bin/activate && python reset_schema.py"' >> ~/.bashrc && source ~/.bashrc
