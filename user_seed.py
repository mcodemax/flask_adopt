"""Seed file for Adoptions"""

from models import Pet, db
from app import app



# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()



# Add Pets
Pet1 = Pet(name="snuggles", species="Bunny", age=1, notes="He cuddly", available=True)
Pet2 = Pet(name="shark", species="goldfish", photo_url="https://thumbs-prod.si-cdn.com/YsbSfQ1_3SVZDnTF1MAjE7wpj_Q=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/c3/60/c3602e77-84ac-423a-aaa1-e4bfbd035afb/e5ull2hxoam59uy.jpeg",
         notes="blublub", available=False)
Pet3 = Pet(name="Champ", species="Dog", age=5, photo_url="https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg",
         available=True)
Pet4 = Pet(name='Onlyhasfirstname', species="Idk", available=False)

# Add new objects to session, so they'll persist
db.session.add(Pet1)
db.session.add(Pet2)
db.session.add(Pet3)
db.session.add(Pet4)

# Commit--otherwise, this never gets saved!
db.session.commit()
