import os
import pandas as pd

def read_csv_files(input_path):
    """
    Function to process CSV files in a folder and concatenate them into a single DataFrame.
    """
    # Create an empty list to store DataFrames
    dfs = []

    # Loop through CSV files in the folder
    for filename in os.listdir(input_path):
        if filename.endswith(".csv"):  # Check if it's a CSV file
            file_name = os.path.splitext(filename)[0]
            df = pd.read_csv(os.path.join(input_path, filename))
            df['file_name'] = file_name
            dfs.append(df)

    # Concatenate the DataFrames into a single DataFrame
    concatenated_df = pd.concat(dfs, ignore_index=True)

    return concatenated_df
