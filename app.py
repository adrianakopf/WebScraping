from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    result = mongo.db.mars.find_one()
    return render_template("index.html", result=result)


@app.route("/scrape")
def scrape():
    result = mongo.db.result
    mars_data = scrape_mars.scrape()
    # print("After calling scrape");
    # print(mars_data)
    result.update(
        {},
        mars_data,
        upsert=True
    )
    print("Done Inserting");
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)