import pandas as pd
import sqlalchemy

# Step 1: EXTRACT - Read the data
# Replace 'your_file.csv' with the path to your file
df = pd.read_csv("C:\Users\risha\Desktop\Annexure data set  to be used.xlsx")

# (Optional) If the data is stored in a database, you can extract it using SQLAlchemy
# db_engine = sqlalchemy.create_engine('mysql://user:password@localhost/dbname')
# df = pd.read_sql("SELECT * FROM your_table", con=db_engine)

# Step 2: TRANSFORM - Data cleaning and transformations
def clean_and_transform(df):
    # Example transformation: Drop rows with missing values
    df.dropna(inplace=True)

    # Example transformation: Convert 'date_column' to datetime format
    df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

    # Example transformation: Create a new column based on an existing column
    df['new_column'] = df['existing_column'] * 2

    # Example transformation: Rename columns for better clarity
    df.rename(columns={'old_name': 'new_name'}, inplace=True)

    # Example transformation: Filter the rows where a condition is met
    df = df[df['numeric_column'] > 100]

    return df

# Apply the transformation function to the DataFrame
df_transformed = clean_and_transform(df)

# Step 3: LOAD - Save the transformed data
# Save the cleaned DataFrame to a new CSV
df_transformed.to_csv('transformed_data.csv', index=False)

# (Optional) Load the transformed data into a SQL database
# df_transformed.to_sql('transformed_table', con=db_engine, if_exists='replace', index=False)

print("ETL process completed. Transformed data saved to 'transformed_data.csv'.")
