import csv

all_articles = []
with open("english_articles.csv") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []
