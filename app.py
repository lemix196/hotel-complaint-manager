from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return "This is index page"

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    return "This is complaint page"

@app.route('/complaints/<user>')
def index():
    return "This is user complaints page"

@app.route('/ratings')
def index():
    return "This is ratings page"



if __name__ == "__main__":
    app.run()