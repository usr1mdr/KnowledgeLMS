from db import database_query
from test import Scrape
from dag import Node, Edge, Base, mymetadata
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, select

# url = 'https://www.matterport.com'
# scrape = Scrape()
# engine = create_engine('sqlite://')
# Base.metadata.create_all(engine)
# session = sessionmaker(engine)()

url = "https://matterport.com/solutions/property-marketing"
x = Scrape()
x.test_url(url)
x.scrape()
print(x)
# n1 = Node()
# n2 = Node()
# n3 = Node()
# Edge(n1,n2)
# Edge(n2,n3)
# table_nodes = n1.__table__
# table_edges = Edge.__table__
# session.add_all([n1,n2])
# session.commit()

# out = select(table_edges)
# sel_com = session.execute(out)
# for item in sel_com:
#     print(item)

# for item in mymetadata.sorted_tables:
#     print(item.c)
    # print(item.name)

# assert [x for x in n2.lower_neighbors()] == [n1]