from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, ValidationError, URL, AnyOf
from models import MAX_NOTE_LEN, MAX_STR_LEN

class AddPetForm(FlaskForm):
    """Form for adding Pets"""

    name = StringField("Pet Name", 
                        validators=[InputRequired(), Length(min=1, max=MAX_STR_LEN)])
                                
    species = StringField("Pet Species", 
                        validators=[InputRequired(), Length(min=1, max=MAX_STR_LEN), AnyOf(values=['cat', 'dog', 'porcupine'])])  

    photo_url = StringField("Pet's Photo Url", 
                        validators=[Optional(), Length(min=1, max=MAX_NOTE_LEN), URL(require_tld=False)])

    age = IntegerField("Pet's Age",
                        validators=[Optional(), NumberRange(min=0, max=30)
                        ])

    notes = StringField("Pet Notes", 
                        validators=[Optional()])

    available = BooleanField("Available?",
                        validators=[Optional()]) #might not need input req for a checkbox

class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField("Change Pet's Photo Url", 
                        validators=[Optional(), Length(min=1, max=MAX_NOTE_LEN), URL(require_tld=False)])

    notes = StringField("Edit Pet Notes", 
                        validators=[Optional()])

    available = BooleanField("Available?",
                        validators=[Optional()]) #might not need input req for a checkbox
