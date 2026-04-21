import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure()
    df[column].hist()
    plt.title(f"Histogram of {column}")
    return plt

def plot_correlation(df):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True)
    plt.title("Correlation Heatmap")
    return plt