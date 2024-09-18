from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Customer, Base

# Database connection details (replace with your own)
engine = create_engine('sqlite:///app/pharmacy.db')
Session = sessionmaker(bind=engine)
session = Session()

# Faker instance for generating random data
fake = Faker()

# Generate a list of customer names
customer_names = [
    "John Doe", "Jane Smith", "Alice Johnson", "Bob Williams", "Emily Davis"
]

# Shuffle the customer names to randomize the order
fake.random.shuffle(customer_names)