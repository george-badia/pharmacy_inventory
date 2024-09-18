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