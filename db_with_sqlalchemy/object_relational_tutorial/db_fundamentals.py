from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import and_, or_, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import aliased, relationship, sessionmaker
from sqlalchemy.orm import selectinload, joinedload, contains_eager
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.sql import exists, func

# Declarative mapping
# - maintains a catalog of classes and tables
Base = declarative_base()


# Mapping classes to Base
# Requirements:
# - __tablename__: must be assigned a table name
# - at least one Column which is part of a primary key
#
# Using the Declarative system a table metadata is created and can be accessed via
# - User.__table__
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<user(name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}'>"


if __name__ == "__main__":

    # Create an engine instance, not to be confused with a connection
    # - using a in-memory-only SQLite database
    # - echo: shortcut to setup SQLAlchemy logging
    engine = create_engine("sqlite:///:memory", echo=True)

    # Create table schema
    Base.metadata.create_all(engine)

    # Creating an instance of a mapped class
    user = User(name="et", fullname="Eric ...", nickname="NetworkPistol")

    print("User object details")
    print("-" * 80)
    print(f"user.name = {user.name}")
    print(f"user.nickname = {user.nickname}")
    print(f"user.id = {user.id}")
    print()

    # Setup the ORM's handle to the database but no connection is opened
    # Once it's first used, a connection is retrieved from a a pool of connections
    Session = sessionmaker(bind=engine)

    # Create an Session instance
    session = Session()

    # Persist the User object
    # - pending,no SQL has been issued
    # - Session will flush the SQL as soon as is needed
    # - if the db is queried, all pending information will first be flushed and then query the db
    #   this can be seen in the logs
    session.add(user)

    # Query db
    query_user = session.query(User).filter_by(name="et").first()
    print(query_user)

    # Session keeps an internal map of object so if the object exists it will return the same instance
    # - it uses the primary key
    print(f"user in query_user = {user in session}")

    # Adding multiple ojbects
    session.add_all(
        [
            User(name='wendy', fullname='Wendy Williams', nickname='windy'),
            User(name='mary', fullname='Mary Contrary', nickname='mary'),
            User(name='fred', fullname='Fred Flintstone', nickname='freddy')
        ]
    )

    # Changing an object's attribute
    user.nickname = "NetworkPistolero"

    # Sessions knows when objects have been modified
    print(f"session.dirty = {session.dirty}")

    # Session knows when objects are pending
    print(f"session.new = {session.new}")

    # Commit changes
    # - it will issue a update SQL statement for the modified object
    # - it will issue a insert SQL statement for each the new object
    #
    # Commit Operations
    # - flush out pending SQL statements
    # - commit transaction to database
    # - session connection resources returned to the connection pool
    session.commit()

    print("User details after commited")
    print("-" * 80)
    print(f"user.name = {user.name}")
    print(f"user.nickname = {user.nickname}")
    print(f"user.id = {user.id}")
    print()

    # Adding erroneous data
    user.name = "Erik"
    fake_user = User(name="fakeuser", fullname="Invalid", nickname="12345")

    # Querying the users
    print(f"Query results: {session.query(User).filter(User.name.in_(['Erik', 'fakeuser'])).all()}")

    # Rollback changes
    # - since it has not been committed
    session.rollback()
    print(user)
    print(f"fake_user in session = {fake_user in session}")

    # Querying
    # - Session.query()
    print("Query User table order by id")
    print("-" * 80)
    for instance in session.query(User).order_by(User.id):
        print(f"{instance.name} - {instance.fullname}")

    # Querying using ORM-instrumented descriptors
    print("Query User table via ORM-instrumented descriptors")
    print("-" * 80)
    for name, fullname in session.query(User.name, User.fullname):
        print(f"{name} - {fullname}")

    # Accessing query by KeyedTuple
    print("Query User table and using KeyedTuple")
    print("-" * 80)
    for record in session.query(User, User.name).all():
        print(f"{record.name} - {record.User}")

    # Querying and renaming columns
    print("Query User table and using a label")
    print("-" * 80)
    for record in session.query(User.name.label("name_label")).all():
        print(record.name_label)

    # Creating alias names for ORM objects
    user_alias = aliased(User, name="user_alias")

    print("Query User table with an alias name")
    print("-" * 80)
    for record in session.query(user_alias, user_alias.name).all():
        print(record.user_alias)

    # Query with limits via Python slices
    for record in session.query(User).order_by(User.id)[1:3]:
        print(record)

    # Common filter operators
    # - ==
    session.query(User).filter(User.name == "et")

    # - !=
    session.query(User).filter(User.name != "et")

    # - like <- depending on backed SQL, may or may not be case sensitive
    session.query(User).filter(User.name.like("%et%"))

    # - ilike <- always case insensitive
    session.query(User).filter(User.name.ilike("%et%"))

    # - in_
    session.query(User).filter(User.name.in_(["et", "wendy", "jack"]))
    session.query(User).filter(User.name.in_(session.query(User.name).filter(User.name.like("%et%"))))

    # - ~ <- notin_
    session.query(User).filter(~User.name.in_(["et", "wendy", "jack"]))

    # - is_
    session.query(User).filter(User.name == None)
    session.query(User).filter(User.name.is_(None)) # Alternative pep8

    # - isnot
    session.query(User).filter(User.name != None)
    session.query(User).filter(User.name.isnot(None))  # Alternative pep8

    # - and_
    session.query(User).filter(and_(User.name == "et", User.fullname == "Eric ..."))

    # - or_
    session.query(User).filter(or_(User.name == "et", User.name == "wendy"))

    # - match <- db backend specific MATCH or CONTAINS function, vary by backend and my not be available
    session.query(User).filter(User.name.match("wendy"))

    # Returning lists and scalars
    # query for all names that have an e
    query = session.query(User).filter(User.name.like("%e%")).order_by(User.id)
    print(f"Results: {query.all()}")
    print(f"First: {query.first()}")
    try:
        print(f"One: {query.one()}")
    except MultipleResultsFound:
        print("One - MultipleResultsFound exception")

    try:
        print(f"one: {query.filter(User.id == 99).one()}")
    except NoResultFound:
        print("One - NoResultFound exception")

    print(f"One or None: {query.filter(User.id == 99).one_or_none()}")

    query = session.query(User).filter(User.name.like("%e%")).order_by(User.id)
    try:
        # Returns the one row or None, if more than one in results then a MultipleResultsFound exception
        print(f"Scalar: {query.scalar()}")
    except MultipleResultsFound:
        print("Scalar - MultipleResultsFound")

    # Textual SQL using sqlalchemy.text
    for user in session.query(User).filter(text("id<224")).order_by(text("id")).all():
        print(user.name)

    # Binding parameters
    print("Querying with binding parameters")
    print(session.query(User).filter(text("id<:value and name=:name")).params(value=224, name="fred").order_by(User.id).one())

    # String-based statement
    print("Querying with String-based statement")
    print(session.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(name="et").all())

    # Passing positional arguments
    stmt = text("SELECT name, id, fullname, nickname FROM users where name=:name")
    stmt = stmt.columns(User.name, User.id, User.fullname, User.nickname)
    print("Querying with positional arguments")
    print(session.query(User).from_statement(stmt).params(name="et").all())

    # Query with specific columns for return
    stmt = text("SELECT name, id, fullname, nickname FROM users where name=:name")
    stmt = stmt.columns(User.name, User.id, User.fullname, User.nickname)
    print("Querying with specific returned columns")
    print(session.query(User.id, User.name).from_statement(stmt).params(name="et").all())

    # Counting
    print(f"The query returned {session.query(User).filter(User.name.like('%e%')).count()} rows")

    # Building a relationship
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

    # one (User) to many (Address)
    # - relationship to: Address.user
    User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

    # To create the new addresses table
    Base.metadata.create_all(engine)

    # Creating a user will have a blank addresses collection
    jack = User(name="jack", fullname="Jack Bean", nickname="jackie")
    print(f"User jack: {jack}")
    print(f"jack.addreses: {jack.addresses}")

    # Adding addresses
    jack.addresses = [
        Address(email_address="jack@google.com"),
        Address(email_address="j25@yahoo.com")
    ]

    # Testing bidirectional relationship
    print(f"jack.addresses[1] = {jack.addresses[1]}")
    print(f"jack.addresses[1].user = {jack.addresses[1].user}")

    # Add user to session and commit
    session.add(jack)
    session.commit()

    # Querying database for jack
    try:
        jack = session.query(User).filter_by(name="jack").one()
        print(f"Query result: {jack}")
        print(f"jack.addresses = {jack.addresses}")
    except MultipleResultsFound:
        print("MultipleResultsFound exception")

    # Querying without Joins
    print("Querying without Join")
    for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(Address.email_address == "jack@google.com").all():
        print(u)
        print(a)
        print()

    # Querying with Joins
    print("Querying with Join")
    for u in session.query(User).join(Address).filter(Address.email_address == "jack@google.com").all():
        print(u)
        print()

        # Querying with OuterJoins
        print("Querying with OuterJoin")
        for u in session.query(User).outerjoin(User.addresses):
            print(u)
            print()

    # Using Aliases so a table can be used twice
    # eg: query that selects a user with two distinct email addresses
    addr_alias1 = aliased(Address)
    addr_alias2 = aliased(Address)

    print("Querying using aliased tables")
    for username, email1, email2 in \
        session.query(User.name, addr_alias1.email_address, addr_alias2.email_address).\
        join(User.addresses.of_type(addr_alias1)). \
        join(User.addresses.of_type(addr_alias2)).\
        filter(addr_alias1.email_address == "jack@google.com").\
        filter(addr_alias2.email_address == "j25@yahoo.com"):
        print(f"username: {username}, email1: {email1}, email2: {email2}")

    # Subqueries
    print("Subquery")
    stmt = session.query(Address.user_id, func.count("*").label("address_count")).group_by(Address.user_id).subquery()
    for u, count in session.query(User, stmt.c.address_count).\
            outerjoin(stmt, User.id == stmt.c.user_id).order_by(User.id):
        print(u, count)

    # Selecting Entities from Subqueries
    stmt = session.query(Address).filter(Address.email_address != "j25@yahoo.com").subquery()
    addr_alias = aliased(Address, stmt)

    for user, address in session.query(User, addr_alias).join(addr_alias, User.addresses):
        print(user)
        print(address)
        print()

    # Using EXISTS
    stmt = exists().where(Address.user_id == User.id)
    for name, in session.query(User.name).filter(stmt):
        print(name)
        print()

    # Common Relationship Operators
    # See website: https://docs.sqlalchemy.org/en/13/orm/tutorial.html

    # Eager loading
    # - selectin load (automatic)
    # - joined load (automatic)
    # - explicit join + eagerload

    # selectin load - intended for loading related collections
    jack = session.query(User).options(selectinload(User.addresses)).filter_by(name="jack").one()
    print(f"selectinload jack: {jack}")
    print(f"selecting loadjack.addresses: {jack.addresses}")

    # Joined load - intended for many to one relationships
    jack = session.query(User).options(joinedload(User.addresses)).filter_by(name="jack").one()
    print(f"joinedload jack: {jack}")
    print(f"joinedload jack.addresses: {jack.addresses}")

    # explicit join + eagerload - useful for pre-loading the many to one object on a query that needs to filter
    # on the same object
    jack_addresses = session.query(Address).join(Address.user).filter(User.name=="jack").options(contains_eager(Address.user)).all()
    print(f"eagerload jack: {jack}")
    print(f"eagerload jack.addresses: {jack.addresses}")

    # Deleting
    print(f"Before deleting jack, count = {session.query(User).filter_by(name='jack').count()}")
    print(f"Jack's addresses, count: {session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count()}")
    session.delete(jack)
    print(f"After deleting jack, count = {session.query(User).filter_by(name='jack').count()}")
    # sqlalchemy will set the address.user to null but will not delete relationships
    jack_addresses = session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com']))
    print(f"Jack's addresses, count: {jack_addresses.count()}")
