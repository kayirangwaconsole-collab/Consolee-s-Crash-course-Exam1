# ============================================
# DRC Education Data Filter Script
# A beginner-friendly script to learn CSV handling
# ============================================

import csv

# STEP 1: Define the input and output file names
# These are the files we'll read from and write to
input_file = "data/sample_education_data.csv"
output_file = "data/DRC_education_corridors.csv"

# STEP 2: Create a list to store the DRC data
# Think of this as an empty container that will hold our filtered rows
drc_rows = []

print("📖 Starting to read the file:", input_file)

# STEP 3: Open and read the input file
# 'with' automatically closes the file when we're done (good practice!)
with open(input_file, 'r') as file:
    # Use csv.DictReader to read the file like a table with column names
    # This makes it easier to access data by column name instead of number
    reader = csv.DictReader(file)
    
    # Get the column headers (first row)
    headers = reader.fieldnames
    print("✓ Found columns:", headers)
    
    # Loop through each row in the file
    for row in reader:
        # Check if the 'Country' column contains 'DRC'
        if row['Country'] == 'DRC':
            # If it's DRC, add this row to our drc_rows list
            drc_rows.append(row)
            print(f"  ✓ Found DRC entry: {row['Region']} - Risk Level: {row['Risk_Level']}")

print(f"\n🔍 Filtered Results: Found {len(drc_rows)} DRC entries\n")

# STEP 4: Write the filtered data to a new file
print("💾 Saving filtered data to:", output_file)

with open(output_file, 'w', newline='') as file:
    # Create a CSV writer for the output file
    writer = csv.DictWriter(file, fieldnames=headers)
    
    # Write the header row
    writer.writeheader()
    
    # Write all the DRC rows we found
    writer.writerows(drc_rows)

print("✓ Done! Your filtered file is ready.")
print(f"\n📊 Summary: Wrote {len(drc_rows)} rows to {output_file}")
