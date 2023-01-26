from sqlalchemy import Column, Table, Integer, String
from config.db import meta, engine

users = Table('users', meta,
              Column('id', Integer, primary_key=True),
              Column('username', String(255), unique=True),
              Column('email', String(255)),
              Column('password', String(255))
              )


meta.create_all(engine)
