from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User,Product

#database connection
DATABASE_URL = 'sqlite:///database.db'


#create a database engine
engine = create_engine(DATABASE_URL)

#create tables in th database
Base.metadata.create_all(engine)

#create a session to interact with the tables
Session = sessionmaker(bind=engine)
session = Session()

#add tables databases
def seed_data():
    #seed users
    user1 = User(name="Enock", email="nyachire@gmail.com")
    user2 = User(name="Stano", email="stang@gmail.com")

    #seed products
    product1 = Product(name="shash",price=50, user=user1)
    product2 = Product(name="quarter",price=250, user=user2)


    #add data to the session
    session.add_all([user1,user2,product1,product2])
    session.commit()


if __name__ == '__main__':
    seed_data()