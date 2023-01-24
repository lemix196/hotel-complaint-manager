from flask import Flask, render_template, url_for, flash, request, redirect
from forms import ComplaintForm, LoginForm, RegisterForm
from models.models import db
from models.complaints import Complaint
from datetime import datetime

# App initialization and configuration
app = Flask(__name__)
app.config.from_pyfile('config.cfg')

# SQLAlchemy DB object initialization
# db = SQLAlchemy(app)
db.init_app(app)


@app.route('/')
def index():
    """Route for homepage"""
    db.create_all()
    return render_template('index.html', active_menu='home')

@app.route('/complaint', methods=['POST', 'GET'])
def complaint():
    """Route with form to add complaint, form fields are based on DB model Complaint"""
    form = ComplaintForm()

    if request.method == "POST" and form.validate_on_submit():
        # When the form is submitted and valid, Complaint object with data from form fields is created,
        # added to db.session and finally saved (commited) to database
        complaint = Complaint(guest_name=form.guest_name.data,
                              room_number=form.room_number.data,
                              message=form.message.data,
                              urgency=form.urgency.data,
                              add_date=datetime.now())
        db.session.add(complaint)
        db.session.commit()
        flash('Your complaint was succesfully sent.')
        return render_template('complaint_summary.html', form=form, active_menu='complaint')
    
    # Function on request method GET renders empty form
    return render_template('complaint.html', form=form, active_menu='complaint')

@app.route('/complaints')
def complaints():
    """Route listing all the complaints stored in database.
       In future it is going to list all complaints added by currently logged user or list all of them for admin"""
    complaints = Complaint.query.all()
    return render_template('complaints.html', complaints=complaints, active_menu='complaints')


@app.route('/complaint/<int:complaint_id>', methods=['POST', 'GET'])
def edit_complaint(complaint_id):
    """Route for editing existing database records. Very similar to adding new complaint, but all the form fields
       are filled with data taken from DB object by its id number. Submitting such form will edit chosen complaint"""
    complaint = Complaint.query.get(complaint_id)
    # Filling form fields with data from DB
    form = ComplaintForm(guest_name=complaint.guest_name,
                         room_number=complaint.room_number,
                         message=complaint.message,
                         urgency=complaint.urgency)

    if request.method == "GET":
        # on method GET: rendering form filled with complaint object data to be edited
        return render_template('edit_complaint.html', form=form, complaint=complaint)

    if request.method == "POST" and form.validate_on_submit():
        # on method POST: change record fields to edited form fields, add current timestamp and commit changes
        complaint.guest_name=form.guest_name.data
        complaint.room_number=form.room_number.data
        complaint.message=form.message.data
        complaint.urgency=form.urgency.data
        complaint.add_date=datetime.now()
        db.session.commit()
        flash(f'Record with id: {complaint_id} succesfully edited!')

    # Show complaints list after successfully editing record
    return redirect(url_for('complaints'))


@app.route('/delete/<int:complaint_id>')
def delete_complaint(complaint_id):
    """Route for deleting complaint from DB"""
    complaint = Complaint.query.get(complaint_id)
    db.session.delete(complaint)
    db.session.commit()
    flash(f'Complaint successfully deleted.')

    # Show complaints list after deleting record
    return redirect(url_for('complaints'))


@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', form=form)

@app.route('/register')
def register():
    form = RegisterForm()

    return render_template('register.html', form=form)

# @app.route('/ratings')
# def ratings():
#     return "This is ratings page"



if __name__ == "__main__":
    app.run()