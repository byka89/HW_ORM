from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id_publ = Column('id_publ', Integer, primary_key=True)
    name = Column('name', String(length=40))

    def __init__(self, id_publ, name):
        self.id_publ = id_publ
        self.name = name

    def __repr__(self):
        return f'({self.id_publ}) {self.name}'


class Book(Base):
    __tablename__ = 'book'
    id_book = Column('id_book', Integer, primary_key=True)
    title = Column('title', String(length=40))
    id_publ = Column('id_publ', Integer, ForeignKey('publisher.id_publ'))

    def __repr__(self):
        return f'{self.title}'


    def __init__(self, id_book, title, id_publ):
        self.id_book = id_book
        self.title = title
        self.id_publ = id_publ


class Shop(Base):
    __tablename__ = 'shop'
    id_shop = Column('id_shop', Integer, primary_key=True)
    name = Column('name', String(length=40))

    def __init__(self, id_shop, name):
        self.id_shop = id_shop
        self.name = name

    def __repr__(self):
        return f'{self.name}'



class Stock(Base):
    __tablename__ = 'stock'
    id_stock = Column('id_stock', Integer, primary_key=True)
    id_book = Column('id_book', Integer, ForeignKey('book.id_book'))
    id_shop = Column('id_shop', Integer, ForeignKey('shop.id_shop'))
    count = Column('count', Integer)

    def __init__(self, id_stok, id_book, id_shop, count):
        self.id_stock = id_stok
        self.id_book = id_book
        self.id_shop = id_shop
        self.count = count


class Sale(Base):
    __tablename__ = 'sale'
    id_price = Column('id_price', Integer, primary_key=True)
    price = Column('price', Integer)
    date_sale = Column('date_sale', Date)
    id_stock = Column('id_stock', Integer, ForeignKey('stock.id_stock'))
    count = Column('count', Integer)

    def __init__(self, id_price, price, date_sale, id_stock, count):
        self.id_price = id_price
        self.price = price
        self.date_sale = date_sale
        self.id_stock = id_stock
        self.count = count

    def __repr__(self):
        return f'{self.price} | {self.date_sale}'



engine = create_engine('postgresql://postgres:1109@localhost:5432/dbalchemy')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

zapros = input()
result = session.query(Book, Shop, Sale).filter(Publisher.name == zapros).filter(Publisher.id_publ == Book.id_publ).filter(Book.id_publ == Stock.id_book).filter(Stock.id_shop == Shop.id_shop).filter(Stock.id_stock == Sale.id_stock).all()
for r in result:
    print(f'{r[0]} | {r[1]} | {r[2]}')


session.close()