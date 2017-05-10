
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    String,
    Integer,
    func,
    DateTime,
    create_engine,
    Boolean,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import sessionmaker
from roomfinder import Base

_val_mapper = lambda value : value if value is not None else ''
#lambda function that is attached to all the Tables
Base.to_dict = lambda self : {key : _val_mapper(val) for key, val in vars(self).items()}


class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    images_uri = Column(JSON)
    property_type = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    address_line_one = Column(String(100), nullable=False)
    popular_counter = Column(Integer, default=0)
    activate = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user = relationship('User', back_populates='properties')
    property_meta = relationship('PropertyMeta', uselist=False, 
                                                 back_populates='property',
                                                 cascade='all, delete, delete-orphan')
    
    @classmethod
    def create_property(cls, json_request):
        if 'id' in json_request:
            del json_request['id']
        return cls(**json_request)
    

        
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    middle_name = Column(String(50))
    last_name = Column(String(50))
    display_name = Column(String(100))
    user_name = Column(String(100), unique=True, nullable=False)
    user_address = Column(String(300))
    contact_number_one = Column(String(20))
    contact_number_two = Column(String(20))
    verified = Column(Boolean, default=False)
    activate = Column(Boolean, default=True)
    password = Column(String(200))
    access_token = Column(String(300), nullable=False)
    photo_uri = Column(String(300))
    cover_photo_uri = Column(String(300))
    email_address = Column(String(300))
    joined_date = Column(DateTime, default=func.now())
    user_type = Column(String(40)) #buyer or seller
    points = Column(Integer, default=0)
    properties = relationship('Property', back_populates='user', cascade='all, delete, delete-orphan')

    @classmethod
    def create_user(cls, json_request):
        if 'id' in json_request:
            del json_request['id']
        return cls(**json_request)




class PropertyMeta(Base):
    __tablename__ = 'propertiesmeta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    district = Column(String(30), nullable=False)
    region = Column(String(30))
    country = Column(String(30))
    condition = Column(String(40))
    comments = Column(JSON)
    expiry_date = Column(DateTime)
    description = Column(String(400))
    property_location = Column(String(50))
    land_size = Column(String(20))
    water_supply = Column(Boolean)
    access_road = Column(Boolean)
    property_id = Column(Integer, ForeignKey('properties.id'))
    property = relationship('Property', back_populates='property_meta')

    
    
    