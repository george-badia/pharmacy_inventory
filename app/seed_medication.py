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
