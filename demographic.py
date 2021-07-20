import pandas as pd

df = pd.read_csv("english_articles.csv")
df = df.sort_values("total_events", ascending=False)
df.to_csv("something.csv")
output = df.head(20).values.tolist()
