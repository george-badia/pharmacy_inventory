from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date, timedelta
from models import Prescription, Customer, Medication, Base

# Database connection details (replace with your own)
engine = create_engine('sqlite:///app/pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define a list of medication instructions
instructions = [
    "Take twice a day w/water",
    "Use once before bedtime",
    "Take on an empty stomach",
    "Apply to skin once daily",
    "Take after meals daily",
    "Swallow 1 pill w/milk",
    "Take 3 times daily w/food",
    "Use before sleep nightly",
    "Take every 4 hours daily",
    "Dissolve in water once",
    "Take with breakfast daily",
    "Inhale 2 puffs as needed",
    "Take once a day w/food",
    "Use for 7 days at night",
    "Take 1 hour before food"
]