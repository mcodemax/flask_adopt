"""Models for Adoption Agency."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

MAX_STR_LEN = 50
MAX_NOTE_LEN = 5000

class Pet(db.Model): # usually only run this once after deployment otherwise you'll constantly be recreating data
    """Pet."""
    __tablename__ = "pets"

    def __repr__(self):
        return f"""<Pet id={self.id} name={self.name} species={self.species} photo_url={self.photo_url}
                age={self.age} notes={self.notes} available={self.available}>"""

    id = db.Column(db.Integer, # int not the same as SQL Integer, the ORM translates etween python and postgreSQL
                    primary_key=True,
                    autoincrement=True)
    
    name = db.Column(db.String(MAX_STR_LEN),
                            nullable=False)

    species = db.Column(db.String(MAX_STR_LEN)) #maybe null as default?

    photo_url = db.Column(db.String(MAX_NOTE_LEN))
                            
    age = db.Column(db.Integer)

    notes = db.Column(db.String(MAX_NOTE_LEN))                        

    available = db.Column(db.Boolean,
                            default=True)


    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete 

