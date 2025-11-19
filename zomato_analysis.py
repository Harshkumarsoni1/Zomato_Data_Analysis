import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zomato_dataset.csv')
print(df.head())

# Simple histogram
df['rating'].hist()
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("rating_plot.png")