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

# Generate some random dates for prescriptions 
from_date = date(2024, 8, 1)  
to_date = date.today()  

# Function to generate a random date within a specified range
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_since_start = int(time_between_dates.days * random.random())
    return start_date + timedelta(days=days_since_start)


import random

# Seed 20 prescriptions 
for _ in range(20):
    # Get random customer and medication IDs 
    customer_id = random.randint(1, 5)  
    medication_id = random.randint(1, len(session.query(Medication).all()))  

    # Generate a random quantity and date
    quantity = random.randint(10, 30)  
    date_issued = generate_random_date(from_date, to_date)

# Select a random instruction
    instruction = random.choice(instructions)

    # Create a new prescription
    prescription = Prescription(
        customer_id=customer_id,
        medication_id=medication_id,
        quantity=quantity,
        date_issued=date_issued,
        instruction=instruction  
    )

    # Add the prescription to the session
    session.add(prescription)

# Commit the changes to the database
session.commit()

print(f"Successfully created {len(session.query(Prescription).all())} prescriptions!")

