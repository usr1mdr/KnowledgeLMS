from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)
class Node(Base):
    __tablename__ = "node"

    node_id = Column(Integer, primary_key=True)

    def higher_neighbors(self):
        return [x.higher_node for x in self.lower_edges]

    def lower_neighbors(self):
        return [x.lower_node for x in self.higher_edges]

class Edge(Base):
    __tablename__ = "edge"

    lower_id = Column(Integer, ForeignKey("node.node_id"), primary_key=True)

    higher_id = Column(Integer, ForeignKey("node.node_id"), primary_key=True)

    lower_node = relationship(
        Node, primaryjoin=lower_id == Node.node_id, backref="lower_edges"
    )

    higher_node = relationship(
        Node, primaryjoin=higher_id == Node.node_id, backref="higher_edges"
    )

    def __init__(self, n1, n2):
        self.lower_node = n1
        self.higher_node = n2

class PageContent(Base):
    __tablename__ = "page"

    page_id = Column(Integer, ForeignKey("node.node_id"), primary_key = True)
    page_url = Column(String)
    page_content = Column(String)

