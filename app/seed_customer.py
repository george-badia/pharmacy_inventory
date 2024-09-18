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

# Create a list of customers
customers = []
for name in customer_names:
    phone = fake.phone_number()
    email = fake.email()
    customers.append(Customer(name=name, phone=phone, email=email))

# Add all customers to the session
session.add_all(customers)

# Commit the changes to the database
session.commit()

print(f"Successfully created {len(customers)} customers!")