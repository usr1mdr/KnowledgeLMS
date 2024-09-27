from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
# from dag import Node, Edge

class database_query():
    def __init__(self):
        self.var = ''
        # self.Base = declarative_base()
        # self.engine = create_engine("sqlite://", echo=True)
        # self.Base.metadata.create_all(self.engine)
        # self.session = sessionmaker(self.engine)()

    # def dag_func(self):
        # node_table_name = 'node'
        # node = Node()
        # edge = Edge()
        # n1 = node
        # n2 = node
        # e1 = edge(n1,n2)
        # self.session.add_all([n1,n2,e1])
        # self.session.commit()
    
    # def exec_sql(self, query):
    #     with self.engine.connect() as conn:
    #         for row in conn.execute(query):
    #             print(row)
        
    def select_func(self, table_in):
        __table_name__ = table_in
        Base = declarative_base()
        engine = create_engine("sqlite://", echo=True)
        Base.metadata.create_all(engine)
        session = sessionmaker(engine)()
        stmt = select(table_in)
        print(stmt)


        # __table_name__ = 'node'
        # print(type(__table_name__))
        # node = Node(table_name)
        # user_table = 'links'
        # stmt = select(Node(table_name))
        # for row in self.session.execute(stmt):
            # print(row)
        # result = self.session.execute('SELECT * FROM links').fetchall()
        # with self.engine.connect() as conn:
        #     for row in conn.execute(stmt):
        #         print(row)

        self.session.close()


        # engine = connect('sqlite:///links.db', echo=True)
    
    