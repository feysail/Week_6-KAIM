import pandas as pd
def data_average(data):
    return data.groupby('CustomerId')[['Amount']].mean().sort_index(ascending=False)
def data_count(data):
    return data.groupby('CustomerId')[['Amount']].count().sort_index(ascending=False)
def data_std(data):
    return data.groupby('CustomerId')[['Amount']].std().sort_index(ascending=False)

def encode(val):
    if val=='airtime':
        return 0
    elif val=='financial_services':
        return 1
    elif val=='utility_bill':
        return 2
    elif val=='data_bundles':
        return 3
    elif val=='tv':
        return 4
    elif val=='transport':  
        return 5
    elif val=='ticket':
        return 6
    elif val== 'movies':
        return 7
    elif  val=='other':
        return 8