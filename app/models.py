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


    # Add class methods for CRUD functionality
    @classmethod
    def create(cls, session, name, phone, email):
        new_customer = cls(name=name, phone=phone, email=email)
        session.add(new_customer)
        session.commit()

    @classmethod
    def delete(cls, session, customer_id):
        customer = session.query(cls).get(customer_id)
        if customer:
            session.delete(customer)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, customer_id):
        return session.query(cls).get(customer_id)

#  Medication Model
class Medication(Base):
    __tablename__ = 'medication'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
   #Add relationship to medication
    # prescriptions = relationship('Prescription', back_populates='medication')
    prescriptions = relationship('Prescription', back_populates='medication', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Medication(name={self.name}, quantity={self.quantity}, price={self.price})>"

    
    #add class methods for CRUD functionality
    @classmethod
    def create(cls, session, name, description, quantity, price):
        new_medication = cls(name=name, description=description, quantity=quantity, price=price)
        session.add(new_medication)
        session.commit()

    @classmethod
    def delete(cls, session, medication_id):
        medication = session.query(cls).get(medication_id)
        if medication:
            session.delete(medication)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, medication_id):
        return session.query(cls).get(medication_id)


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
    
     #Add class methods to perform Crud functionality    
    @classmethod
    def create(cls, session, customer_id, medication_id, quantity, date_issued, instruction):
        new_prescription = cls(customer_id=customer_id, medication_id=medication_id, quantity=quantity, date_issued=date_issued, instruction=instruction)
        session.add(new_prescription)
        session.commit()

    @classmethod
    def delete(cls, session, prescription_id):
        prescription = session.query(cls).get(prescription_id)
        if prescription:
            session.delete(prescription)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, prescription_id):
        return session.query(cls).get(prescription_id)

#User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


    def __repr__(self):
        return f"<User:(username={self.username}, password={self.password})>"
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()



    @classmethod
    def authenticate(cls, session, username, password):
        user = session.query(cls).filter_by(username=username).first()
        if user and cls.hash_password(password) == user.password:
            return True
        return False

# Create an SQLite database engine
engine = create_engine('sqlite:///app/pharmacy.db')

# Create the database schema (all tables)
Base.metadata.create_all(engine)

# Create a session factory bound to the engine
Session = sessionmaker(bind=engine)
def get_session():
    """Yield a new database session."""
    session = Session()
    try:
        yield session
    finally:
        session.close()

             