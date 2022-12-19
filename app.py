from flask import Flask, render_template, url_for
from forms import ComplaintForm

app = Flask(__name__)

@app.route('/')
def index():
    return "This is index page"

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    form = ComplaintForm()
    return render_template("complaint.html", form=form)

@app.route('/complaints/<user>')
def index():
    return "This is user complaints page"

@app.route('/ratings')
def index():
    return "This is ratings page"



if __name__ == "__main__":
    app.run()