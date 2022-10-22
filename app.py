from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Redirect to home page"""
    
    return redirect('/pets')

@app.route('/pets')
def pets_list():
    """Display list of pets"""

    pets = Pet.query.all()

    return render_template('pets-list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def new_pet():
    """Generate form to add pet and handle form submission"""

    form = NewPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()

        return redirect('/pets')
    else:
        return render_template('pets-new.html', form=form)

@app.route('/<int:id>', methods=["GET","POST"])
def pet_details(id):
    """Display list of pets"""

    form = EditPetForm()
    pet = Pet.query.get_or_404(id)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect('/pets')
    else:
        return render_template('pet-details.html', pet=pet, form=form)

    
