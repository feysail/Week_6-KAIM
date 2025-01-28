import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
def univarate(data):
    df_num = data.select_dtypes(include = ['float64', 'int64'])
    return df_num.hist(figsize = (15, 10), bins = 50)