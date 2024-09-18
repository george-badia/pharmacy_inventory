from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Define the declarative base class
Base = declarative_base()


# Customer model
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Add relationship to Prescription
    prescriptions = relationship('Prescription', back_populates='customer')

    def __repr__(self):
        return f"<Customer:(name={self.name}, phone={self.phone}, email={self.email})>"

#  Medication Model
class Medication(Base):
    __tablename__ = 'medication'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

   #Add relationship to medication
    prescriptions = relationship('Prescription', back_populates='medication')


    def __repr__(self):
        return f'<Medication:(id={self.id}, name="{self.name}")>'


#  Prescription Model
class Prescription(Base):
    __tablename__ = 'prescription'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    medication_id = Column(Integer, ForeignKey('medication.id'), nullable=False) 
    quantity = Column(Integer, nullable=False)
    date_issued = Column(Date, nullable=False)
    instruction = Column(String, nullable=False)

    #add relationship to customer and medication
    customer = relationship('Customer', back_populates='prescriptions')
    medication = relationship('Medication', back_populates='prescriptions')

    def __repr__(self):
        return f"<Prescription:(customer_id={self.customer_id}, medication_id={self.medication_id}, quantity={self.quantity}, date_issued={self.date_issued} instruction={self.instruction})>"

