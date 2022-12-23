from flask import Flask, render_template, url_for, flash, request
from forms import ComplaintForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

# DB Models

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(50))
    room_number = db.Column(db.Integer)
    message = db.Column(db.String(500))
    urgency = db.Column(db.String(15))


# End of DB models

@app.route('/')
def index():
    db.create_all()
    return render_template('index.html', active_menu='home')

@app.route('/complaint', methods=['POST', 'GET'])
def complaint():
    form = ComplaintForm()
    if request.method == "POST" and form.validate_on_submit():
        complaint = Complaint(guest_name=form.guest_name.data,
                              room_number=form.room_number.data,
                              message=form.message.data,
                              urgency=form.urgency.data)
        db.session.add(complaint)
        db.session.commit()
        flash('Your complaint was succesfully sent.')
        return render_template('complaint_summary.html', form=form, active_menu='complaint')
    
    return render_template('complaint.html', form=form, active_menu='complaint')

# @app.route('/complaints/<user>')
# def list_user_complaints():
#     return "This is user complaints page"

@app.route('/ratings')
def ratings():
    return "This is ratings page"



if __name__ == "__main__":
    app.run()