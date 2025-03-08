import csv

# Define the input and output CSV file paths
input_file = 'D:/GOKUL-UG/VIT/Assignments/Sem3/SEM/project/dbdata.csv'
output_file = 'D:/GOKUL-UG/VIT/Assignments/Sem3/SEM/project/dbdata_quoted.csv'

# Open the input CSV file and read its contents
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    
    # Open the output CSV file to write the processed data
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Iterate through each row in the input file
        for row in reader:
            # Loop through each field in the row
            row = [f'"{field}"' if ',' in field else field for field in row]
            # Write the processed row to the output file
            writer.writerow(row)

print(f"Processed CSV with quoted fields saved to {output_file}")
