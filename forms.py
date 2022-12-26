from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField

#later on add validators to that class
class ComplaintForm(FlaskForm):

    _URGENCY_LIST = [("normal", "normal"),
                     ("high", "high"),
                     ("emergency", "emergency")
                    ]


    guest_name = StringField(u"Full guest name")
    room_number = IntegerField(u"Room number")
    message = StringField(u"Tell us about your inconvenience")
    urgency = SelectField(u"Urgency", choices=_URGENCY_LIST)


if __name__ == "__main__":
    pass
