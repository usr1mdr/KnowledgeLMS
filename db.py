from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, inspect
# from dag import Node, Edge

class database_query():
    def __init__(self):
        self.var = ''
        
    def select_func(self, table_in=None):
        __table_name__ = table_in
        Base = declarative_base()
        engine = create_engine("sqlite:///nodes.db", echo=True)
        mymetadata = Base.metadata.create_all(engine)
        session = sessionmaker(engine)()

        if table_in is None:
            for item in mymetadata.sorted_tables:
                print(item.c)
                print(item.name)
        # stmt = select(table_in)
        # print(stmt)

        # Inspecting the Schema
        if table_in is not None:
            inspector = inspect(engine)
            columns = inspector.get_columns('node')
            for column in columns:
                print(f"Column: {column['name']}, Type: {column['type']}, Auto-Increment: {column['autoincrement']}")
            self.session.close()
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

x = database_query()
x.select_func()
        # engine = connect('sqlite:///links.db', echo=True)
    
    