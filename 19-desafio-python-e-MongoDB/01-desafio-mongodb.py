import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    
    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascado="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, auto_increment=True)
    email_address = Column(String(30), nullable=False)
    User_id = Column(Integer, ForeignKey("user_account.id"), nullable = False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Adress(id={self.id}, email={self.email_address})"