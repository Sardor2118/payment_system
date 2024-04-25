from database import Base
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(55), nullable=False)
    surename = Column(String(55), nullable=False)
    user_photo = Column(String)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


class Card(Base):
    __tablename__ = "cards"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    card_number = Column(BigInteger, nullable=False, unique=True)
    exp_date = Column(Integer, nullable=False)
    card_balance = Column(Float, nullable=False)
    cvv = Column(Integer, nullable=False)
    card_name = Column(String, nullable=False)
    reg_date = Column(DateTime, nullable=False)

    user = relationship(User, lazy="subquery")


class Transactions(Base):
    __tablename__ = "user_transactions"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    card_from = Column(BigInteger, ForeignKey("cards.card_number"), nullable=False)
    amount = Column(Float, nullable=False)
    card_to = Column(BigInteger, ForeignKey("cards.card_number"), nullable=False)
    transfer_time = Column(DateTime, nullable=False)

    card_from_fk = relationship(Card, lazy="subquery")
    card_to_fk = relationship(Card, lazy="subquery")