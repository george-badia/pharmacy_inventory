import argparse
import re
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import Session
from models import Customer, Medication, Prescription, User, get_session
import re
from datetime import datetime
from sqlalchemy.orm import Session
from models import Customer, Medication, Prescription, User, get_session

class Pharmacy:
    def __init__(self):
        self.session = next(get_session())

    def add_medication(self):
        name = input("Enter medication name: ")
        description = input("Enter medication description (optional): ")
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity < 0:
                    raise ValueError("Quantity must be non-negative")
                break
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
        while True:
            try:
                price = float(input("Enter medication price: "))
                if price < 0:
                    raise ValueError("Price must be non-negative")
                break
            except ValueError:
                print("Invalid price. Please enter a valid number.")
        
        try:
            Medication.create(self.session, name, description, quantity, price)
            print(f"Medication '{name}' added successfully.")
        except:
            self.session.rollback()
            print(f"Failed to add medication '{name}'.")

    def delete_medication(self):
        medication_id = input("Enter medication ID to delete: ")
        try:
            medication_id = int(medication_id)
            Medication.delete(self.session, medication_id)
            print(f"Medication with ID {medication_id} deleted successfully.")
        except ValueError:
            print("Invalid ID. Please enter a number.")
        except:
            self.session.rollback()
            print(f"Failed to delete medication with ID {medication_id}.")

    def display_medications(self):
        medications = Medication.get_all(self.session)
        if not medications:
            print("No medications available.")
        else:
            for med in medications:
                print(f"ID: {med.id}, Name: {med.name}, Quantity: {med.quantity}, Price: ${med.price:.2f}")

    def add_customer(self):
        name = input("Enter customer name: ")
        while True:
            phone = input("Enter customer phone number: ")
            if re.match(r'^\d{10}$', phone):
                break
            print("Invalid phone number. Please enter a 10-digit number.")
        email = input("Enter customer email: ")
        
        try:
            Customer.create(self.session, name, phone, email)
            print(f"Customer '{name}' added successfully.")
        except:
            self.session.rollback()
            print(f"Failed to add customer '{name}'.")

    def delete_customer(self):
        customer_id = input("Enter customer ID to delete: ")
        try:
            customer_id = int(customer_id)
            Customer.delete(self.session, customer_id)
            print(f"Customer with ID {customer_id} deleted successfully.")
        except ValueError:
            print("Invalid ID. Please enter a number.")
        except:
            self.session.rollback()
            print(f"Failed to delete customer with ID {customer_id}.")

    def display_customers(self):
        customers = Customer.get_all(self.session)
        if not customers:
            print("No customers available.")
        else:
            for customer in customers:
                print(f"ID: {customer.id}, Name: {customer.name}, Phone: {customer.phone}, Email: {customer.email}")

    def add_prescription(self):
        customer_id = input("Enter customer ID: ")
        medication_id = input("Enter medication ID: ")
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be positive")
                break
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
        date_issued = datetime.now().date()
        instruction = input("Enter prescription instruction: ")

        try:
            customer_id = int(customer_id)
            medication_id = int(medication_id)
            Prescription.create(self.session, customer_id, medication_id, quantity, date_issued, instruction)
            print("Prescription added successfully.")
        except ValueError:
            print("Invalid ID. Please enter a number for customer ID and medication ID.")
        except:
            self.session.rollback()
            print("Failed to add prescription.")

    def delete_prescription(self):
        prescription_id = input("Enter prescription ID to delete: ")
        try:
            prescription_id = int(prescription_id)
            Prescription.delete(self.session, prescription_id)
            print(f"Prescription with ID {prescription_id} deleted successfully.")
        except ValueError:
            print("Invalid ID. Please enter a number.")
        except:
            self.session.rollback()
            print(f"Failed to delete prescription with ID {prescription_id}.")

    def generate_sales_report(self):
        prescriptions = Prescription.get_all(self.session)
        if not prescriptions:
            print("No sales data available.")
            return
        total_sales = 0
        print("Sales Report:")
        for prescription in prescriptions:
            sale_amount = prescription.medication.price * prescription.quantity
            total_sales += sale_amount
            print(f"Date: {prescription.date_issued}, Customer: {prescription.customer.name}, "
                  f"Medication: {prescription.medication.name}, Quantity: {prescription.quantity}, "
                  f"Amount: ${sale_amount:.2f}")
        print(f"Total Sales: ${total_sales:.2f}")

def main():
    pharmacy = Pharmacy()
    while True:
        print("\n--- Pharmacy Management System ---")
        print("1. Add Medication")
        print("2. Delete Medication")
        print("3. Display All Medications")
        print("4. Add Customer")
        print("5. Delete Customer")
        print("6. Display All Customers")
        print("7. Add Prescription")
        print("8. Delete Prescription")
        print("9. Generate Sales Report")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            pharmacy.add_medication()
        elif choice == '2':
            pharmacy.delete_medication()
        elif choice == '3':
            pharmacy.display_medications()
        elif choice == '4':
            pharmacy.add_customer()
        elif choice == '5':
            pharmacy.delete_customer()
        elif choice == '6':
            pharmacy.display_customers()
        elif choice == '7':
            pharmacy.add_prescription()
        elif choice == '8':
            pharmacy.delete_prescription()
        elif choice == '9':
            pharmacy.generate_sales_report()
        elif choice == '10':
            print("Thank you for using the Pharmacy Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()