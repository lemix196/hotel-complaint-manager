from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField
from wtforms import widgets

### CUSTOM FIELDS
class PasswordField(StringField):
    widget = widgets.PasswordInput(hide_value=False)

### END OF CUSTOM FIELDS


### FORMS
class ComplaintForm(FlaskForm):

    _URGENCY_LIST = [("normal", "normal"),
                     ("high", "high"),
                     ("emergency", "emergency")
                    ]


    guest_name = StringField(u"Full guest name")
    room_number = IntegerField(u"Room number")
    message = StringField(u"Tell us about your inconvenience")
    urgency = SelectField(u"Urgency", choices=_URGENCY_LIST)


class LoginForm(FlaskForm):
    user_name = StringField(u"Username")
    password = PasswordField(u"Password")


if __name__ == "__main__":
    pass
