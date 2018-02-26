# Dependencies
from flask import Flask, jsonify, render_template, request
import pymongo
import scrape_mars

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars
mars = db.mars

@app.route("/")
def index():
    mars_info = db.mars.find_one()

    return render_template("index_tmplt.html",
    news_title=results[0]['news_title'],
    news_p=results[0]['news_p'],
    featured_image_url=result[0]['featured_image_url'],
    mars_weather=results[0]['mars_weather'],
    profile_html=results[0]['profile_html'])


@app.route("/scrape")
def scrape():
    mars_info = db.mars
    mars_data = scrape_mars.Scrape()
    mars_info.update(
        {},
        mars_data,
        upsert = True
    )

    return index()

if __name__ == "__main__":
    app.run(debug=False)