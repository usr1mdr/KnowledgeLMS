from db import database_query
from dag import Node
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select

# db_instance = database_query()
# db_instance.select_func()
# node = Node()
# table_in = node

# Base = declarative_base()
# engine = create_engine("sqlite://", echo=True)
# Base.metadata.create_all(engine)

# session = sessionmaker(engine)()

n1 = Node()
# session.add_all([n1])
# session.commit()
stmt = select(Node)
print(stmt)

engine = create_engine('sqlite://')

with Session(engine) as session:
    for row in conn.execute(stmt):
        print(row)

# db_instance = database_query()
# db_instance.select_func(Node())

