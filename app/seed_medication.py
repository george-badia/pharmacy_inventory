from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Medication, Base

# Database connection details 
engine = create_engine('sqlite:///app/pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()

# Faker instance for generating random data
fake = Faker()

# Default medication descriptions
medication_descriptions = [
    "Pain relief, anti-inflammatory.",
    "Reduces pain and fever.",
    "Fever and pain reducer.",
    "Broad-spectrum antibiotic.",
    "Blood sugar regulator.",
    "Lowers blood pressure.",
    "Reduces cholesterol levels.",
    "Cholesterol-lowering drug.",
    "Treats acid reflux.",
    "Thyroid hormone replacement."
]

# Medication names 
medication_names = [
    "Aspirin", "Ibuprofen", "Paracetamol", "Amoxicillin", "Metformin",
    "Insulin", "Albuterol", "Salbutamol", "Prednisolone", "Levothyroxine",
    "Simvastatin", "Atenolol", "Losartan", "Enalapril", "Amlodipine"
]

# Shuffle the medication names to randomize the order
fake.random.shuffle(medication_names)

# Define a function to generate a random price
def generate_price(min_price=10.0, max_price=50.0):
    return round(fake.random.uniform(min_price, max_price), 2)
