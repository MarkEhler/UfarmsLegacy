from sqlalchemy import create_engine
import pandas as pd

csv_file = 'usr_tbl_insert.csv'
df = pd.read_csv(csv_file)
#database_name=uframs-dev
database_url = 'your_database_connection_string'
engine = create_engine(database_url)
table_name = 'Users'
df.to_sql(table_name, con=engine, if_exists='append', index=False)

csv_file = 'usr_tbl_insert.csv'
df = pd.read_csv(csv_file)
table_name = 'Ufarms'
df.to_sql(table_name, con=engine, if_exists='append', index=False)
