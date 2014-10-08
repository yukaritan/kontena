from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.sql import *
import os
from collections import *
import re

triggers = OrderedDict()

db_list = []
word_list=[]


engine = create_engine('sqlite:///logs.db', echo=False)

connection = engine.connect()

metadata = MetaData(engine)

try:
    connection.execute(
    """
    CREATE TABLE users (
        triggers VARCHAR
    );
    """
    )
except:
    pass

users = Table('users', metadata, Column('triggers', String()))


def insert_db(text,which="triggers"):

    if which == "triggers":


        connection.execute(
            """                                                                                                  
            INSERT INTO users (triggers) VALUES (?);                                                             
            """,
            text
        )

    else:

        connection.execute(
        """                                                                                         
        INSERT INTO users (triggers) VALUES (?);                                                    
        
        """,
        text
        )


def output_db():
    
    global connection
    global users
    s = select([users])
    result = connection.execute(s) 
    return(result)





