from sqlalchemy import create_engine, text
import pandas as pd

# Database connection setup
db_user = 'postgres'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'
db_name = 'globequestdb'
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Drop the table with CASCADE
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS tourpackage CASCADE"))

# Load data into DataFrame
df = pd.read_csv('dbdata.csv')

# Clean the 'price' column if necessary
df['price'] = df['price'].replace('[^0-9.]', '', regex=True).astype(float)

# Save the DataFrame to PostgreSQL
df.to_sql('tourpackage', engine, if_exists='append', index=False)

print("Data saved to PostgreSQL successfully!")
