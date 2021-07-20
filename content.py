import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("english_articles.csv")
df = df[df["title"].notna()]
count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(df["title"])
cosine_sim = cosine_similarity(count_matrix, count_matrix)
df = df.reset_index()
indices = pd.Series(df.index, index=df["title"])


def get_recommendations(title):
    id_x = indices[title]
    sim_scores = list(enumerate(cosine_sim[id_x]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]
    # return df["title"].iloc[article_indices].values.tolist()
    return df[["title", "text"]].iloc[article_indices].values.tolist()


# print(get_recommendations("pull request first - practical blend",cosine_sim))
