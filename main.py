import pandas as pd

# Update file path as required if you have located the data in a different folder to script
file_path = "vgsales.csv"

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return None

# After checking data types it was found that the Year column was being read as a float, which is incorrect. This function, since Pandas reads the N/A values as NaN, replaces those values with 0000 as a placeholder.
def data_cleaning(data):
    if data is not None:
        data["Year"] = data["Year"].fillna(0000)
        data["Year"] = data["Year"].astype(int)
    return data


def main():
        data = load_data(file_path)
        data = data_cleaning(data)
        if data is not None:
            print(data.head())
        else:
            print("Data loading failed. Please check the file path and contents.")

if __name__ == "__main__":
    main()