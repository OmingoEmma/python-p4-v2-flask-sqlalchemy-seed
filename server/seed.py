#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    fake = Faker()
    Pet.query.delete()

    pets = []

    # Add fixed pets
    pets.append(Pet(name="Fido", species="Dog"))
    pets.append(Pet(name="Whiskers", species="Cat"))
    pets.append(Pet(name="Hermie", species="Hamster"))
    pets.append(Pet(name="Slither", species="Snake"))

    # Add 10 random pets
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    for _ in range(10):
        pets.append(Pet(name=fake.first_name(), species=rc(species))) 
    # Add to DB and commit
    db.session.add_all(pets)
    db.session.commit()
