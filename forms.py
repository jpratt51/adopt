from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange, URL, AnyOf, Optional

class NewPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired(message="Name Cannot Be Blank")])
    species = StringField("Species", validators=[InputRequired(message="Species required"), AnyOf(["dog", "cat", "mouse", "chinchilla", "monkey"])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=False, message="Must be valid URL")])
    age = FloatField("Age in years", validators=[NumberRange(1,30, "Age must be 1-30 years old")])
    notes = StringField("Notes")
    available = BooleanField("Available for Adoption")

class EditPetForm(FlaskForm):

    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=False, message="Must be valid URL")])
    notes = StringField("Notes")
    available = BooleanField("Available for Adoption")