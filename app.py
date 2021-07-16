"""Adoption Agency App"""

from forms import AddPetForm
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5433/adoption' #@ people looking at this code; you may need to change on your own computer for code to work
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True #prints in ipython the queries being run

app.config["SECRET_KEY"] = "maxcode1"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def show_pets():
    """Show all pets"""
    #psql query the db and get a list of users
    pets = Pet.query.all()

    return render_template('homepage.html',pets=pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():
    """Add a pet to the adoption agency"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {field: val for field, val in form.data.items() if field != "csrf_token"}
        #stacked overflow:interating over form fields in flask
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)

    