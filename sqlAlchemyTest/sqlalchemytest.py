# encoding: utf-8

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'empdb'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}/{db}?charset=utf8'.format(username=USERNAME,
                                                                                 password=PASSWORD,
                                                                                 host=HOSTNAME,
                                                                                 port=PORT,
                                                                                 db=DATABASE)
engine = create_engine(DB_URI)

# # 判断是否连接成功
# conn = engine.connect()
# result = conn.execute('select 1')
# print(result.fetchone())

Base = declarative_base(engine)
# Session = sessionmaker(engine)
# session = Session()
session = sessionmaker(engine)()


class Person(Base):
    __tablename__: str = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    mame = Column(String(50))
    age = Column(Integer)
    country = Column(String(50))
