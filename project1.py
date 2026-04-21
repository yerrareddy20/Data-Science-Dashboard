import pandas as pd

def get_basic_info(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns)
    }

def get_summary(df):
    return df.describe()

def get_missing_values(df):
    return df.isnull().sum()