import pandas as pd

# Load the CSV
df = pd.read_csv('D:/GOKUL-UG/VIT/Assignments/Sem3/SEM/project/dbdata.csv')

# Remove duplicates based on 'title' column
df = df.drop_duplicates(subset=['title'])

# Save the cleaned CSV
df.to_csv('cleaned_data.csv', index=False)

