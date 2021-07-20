from flask import Flask, jsonify
from storage import all_articles, liked_articles, not_liked_articles
from demographic import output
from content import get_recommendations

app = Flask(__name__)


@app.route("/get_article")
def get_article():
    return jsonify({"data": all_articles[0], "status": "success"})


@app.route("/like_article", methods=["POST"])
def like_article():
    liked_articles.append(all_articles[0])
    all_articles.pop(0)
    return jsonify({"data": liked_articles, "status": "success"})


@app.route("/not_like_article", methods=["POST"])
def not_like_article():
    not_liked_articles.append(all_articles[0])
    all_articles.pop(0)
    return jsonify({"data": not_liked_articles, "status": "success"})


@app.route("/popular_articles")
def popular():
    return jsonify({"data": output, "status": "success"})


@app.route("/recommended_articles")
def recommended():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[12])
        for data in output:
            all_recommended.append(output)
    import itertools

    all_recommended.sort()
    all_recommended = list(
        all_recommended for all_recommended, _ in itertools.groupby(all_recommended)
    )
    article_data = []
    for article in all_recommended:
        articles_data = {
            "title": article[0],
            "content": article[1],
        }
        article_data.append(articles_data)
    return jsonify({"data": article_data, "status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
