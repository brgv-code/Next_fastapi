# connect  to  the  database testdb as the user root and password 123456789
# and  set  the  default  encoding  to  utf8


from sqlalchemy  import  create_engine, MetaData

engine = create_engine( 'mysql+pymysql://root:123456789@localhost:3306/testdb' )
meta = MetaData(bind=engine)
conn = engine.connect()