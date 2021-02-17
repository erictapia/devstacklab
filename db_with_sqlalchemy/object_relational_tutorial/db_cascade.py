from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker



# Declarative mapping
# - maintains a catalog of classes and tables
Base = declarative_base()


# Configuring delete/delete-orphan cascade
# user class with addresses relationship and cascade configuration
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship("Address", back_populates="user", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"<user(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}'>"

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)

    # ForeignKey constrains value to be a value in the users.id column, users primary key
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationship links the User class to the Address.user
    # - relationship to: User.addresses
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"<Address(email_address={self.email_address}>"


if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all(
        [
            User(name="et", fullname="Eric ...", nickname="NetworkPistol"),
            User(name='wendy', fullname='Wendy Williams', nickname='windy'),
            User(name='mary', fullname='Mary Contrary', nickname='mary'),
            User(name='fred', fullname='Fred Flintstone', nickname='freddy')
        ]
    )

    jack = User(name="jack", fullname="Jack Bean", nickname="jackie")
    jack.addresses = [
        Address(email_address="jack@google.com"),
        Address(email_address="j25@yahoo.com")
    ]
    session.add(jack)
    session.commit()


    # Delete one of Jack's addresses
    jack = session.query(User).get(5)
    del jack.addresses[1]
    print(f"Jack addresses count = {session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count()}")

    # Delete jack
    session.delete(jack)
    print(f"Deleted jack, count = {session.query(User).filter_by(name='jack').count()}")
    print(f"Jack addresses count = {session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count()}")
