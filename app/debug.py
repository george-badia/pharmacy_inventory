#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb;
from models import Medication, Prescription, Customer

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///app/pharmacy.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()