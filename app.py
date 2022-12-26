from flask import Flask, render_template, url_for, flash, request, redirect
from forms import ComplaintForm
from flask_sqlalchemy import SQLAlchemy
from datetime import date

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
    add_date = db.Column(db.DateTime)


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
                              urgency=form.urgency.data,
                              add_date=date.today())
        db.session.add(complaint)
        db.session.commit()
        flash('Your complaint was succesfully sent.')
        return render_template('complaint_summary.html', form=form, active_menu='complaint')
    
    return render_template('complaint.html', form=form, active_menu='complaint')

@app.route('/complaints')
def complaints():
    complaints = Complaint.query.all()
    return render_template('complaints.html', complaints=complaints, active_menu='complaints')


@app.route('/complaint/<int:complaint_id>', methods=['POST', 'GET'])
def edit_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    form = ComplaintForm(guest_name=complaint.guest_name,
                         room_number=complaint.room_number,
                         message=complaint.message,
                         urgency=complaint.urgency)

    if request.method == "GET":
        return render_template('edit_complaint.html', form=form, complaint=complaint)

    if request.method == "POST" and form.validate_on_submit():
        complaint.guest_name=form.guest_name.data
        complaint.room_number=form.room_number.data
        complaint.message=form.message.data
        complaint.urgency=form.urgency.data
        complaint.add_date=date.today()
        db.session.commit()
        flash(f'Record with id: {complaint_id} succesfully edited!')

    return redirect(url_for('complaints'))



# @app.route('/ratings')
# def ratings():
#     return "This is ratings page"



if __name__ == "__main__":
    app.run()