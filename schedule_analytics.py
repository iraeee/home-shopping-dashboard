import pandas as pd
def load_data(path="latest_data.csv"):
    return pd.read_csv(path)
