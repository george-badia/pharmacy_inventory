
import argparse
import re
from rich import print
from rich.table import Table
from rich.console import Console
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import Session
from models import Customer, Medication, Prescription, User, get_session

class Pharmacy:
    def __init__(self):
        self.session = next(get_session())
        self.console = Console()

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
            table = Table(title="Medications")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Quantity", style="green")
            table.add_column("Price", style="yellow")

            for med in medications:
                table.add_row(str(med.id), med.name, str(med.quantity), f"${med.price:.2f}")

            self.console.print(table)

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
            table = Table(title="Customers")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Phone", style="green")
            table.add_column("Email", style="yellow")

            for customer in customers:
                table.add_row(str(customer.id), customer.name, customer.phone, customer.email)

            self.console.print(table)

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

    def display_prescriptions(self):
        prescriptions = Prescription.get_all(self.session)
        if not prescriptions:
            print("No prescriptions available.")
        else:
            table = Table(title="Prescriptions")
            table.add_column("ID", style="cyan")
            table.add_column("Customer", style="magenta")
            table.add_column("Medication", style="green")
            table.add_column("Quantity", style="yellow")
            table.add_column("Date Issued", style="blue")
            table.add_column("Instructions", style="red")

            for prescription in prescriptions:
                # Check if customer and medication are not None
                customer_name = prescription.customer.name if prescription.customer else "Unknown Customer"
                medication_name = prescription.medication.name if prescription.medication else "Unknown Medication"

                table.add_row(
                    str(prescription.id),
                    customer_name,
                    medication_name,
                    str(prescription.quantity),
                    str(prescription.date_issued),
                    prescription.instruction
                )

            self.console.print(table)


    def generate_sales_report(self):
        prescriptions = Prescription.get_all(self.session)
        if not prescriptions:
            print("No sales data available.")
            return

        table = Table(title="Sales Report")
        table.add_column("Date", style="cyan")
        table.add_column("Customer", style="magenta")
        table.add_column("Medication", style="green")
        table.add_column("Quantity", style="yellow")
        table.add_column("Amount", style="red")

        total_sales = 0
        for prescription in prescriptions:
            sale_amount = prescription.medication.price * prescription.quantity
            total_sales += sale_amount
            table.add_row(
                str(prescription.date_issued),
                prescription.customer.name,
                prescription.medication.name,
                str(prescription.quantity),
                f"${sale_amount:.2f}"
            )

        self.console.print(table)
        print(f"Total Sales: ${total_sales:.2f}")

def main():
    pharmacy = Pharmacy()
    while True:
        print("\n=== Pharmacy Management System ===")

        print('---------------------------------------------')
        print("|Enter 1 to  Add Medication                 |")
        print('---------------------------------------------')
        print('|Enter 2 to  Delete Medication              |')
        print('---------------------------------------------')
        print('|Enter 3 to  Display All Medications        |')
        print('---------------------------------------------')
        print('|Enter 4 to  Add Customer                   |')
        print('---------------------------------------------')
        print("|Enter 5 to  Delete Customer                |")
        print('---------------------------------------------')
        print('|Enter 6 to  Display All Customers          |')
        print('---------------------------------------------')
        print('|Enter 7 to  Add Prescription               |')
        print('---------------------------------------------')
        print('|Enter 8 to  Delete Prescription            |')
        print('---------------------------------------------')
        print("|Enter 9 to  Display AllPrescriptions       |")
        print('---------------------------------------------')
        print('|Enter 10 to Generate Sales Report          |')
        print('---------------------------------------------')
        print('|Enter 11 to Exit                           |')
        print('---------------------------------------------')
        


        choice = input("Enter your choice (1-11): ")

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
            pharmacy.display_prescriptions()
        elif choice == '10':
            pharmacy.generate_sales_report()
        elif choice == '11':
            print("Thank you for using the Pharmacy Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()