# import necessary libraries
from flask import Flask, render_template, redirect

from scrape_mars import get_data, get_from_db

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    data = get_from_db()
    if not data:
        return redirect('/scrape')

    return render_template("index.html", text="Mission to Mars", data=data)


@app.route("/scrape")
def scrape():
    get_data()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
