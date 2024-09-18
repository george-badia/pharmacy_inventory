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

