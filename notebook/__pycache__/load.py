import pandas as pd

def load_data(data):
    return pd.read_csv(data)

def overview(data):
    return (f"Rows and colummns {data.shape} respectively")

def Summary_Statistics(data):
    return data.describe()