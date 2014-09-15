#from hooks.basic import *
from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.sql import *
import os

db_list = []
word_list=[]

#if os.path.exists("logs.db"):
   # pass

engine = create_engine('sqlite:///logs.db', echo=False)

connection = engine.connect()

metadata = MetaData(engine)

try:
    connection.execute(
    """
    CREATE TABLE users (
        sentence VARCHAR
    );
    """
    )
except:
    pass

users = Table('users', metadata, Column('sentence', String()))


def hook_db(text = None):
    
    """Used to save what was said"""

    global db_list
    #global word_list
    
    
    db_list.append(text)
    
    connection.execute(
    """
    INSERT INTO users (sentence) VALUES (?);
    """,
    text
    )
    return db_list

def insert_db(text):

    connection.execute(
    """                                                                                                  
    INSERT INTO users (sentence) VALUES (?);                                                             
    """,
    text
    )

def output_db():
    
    global connection
    global users
    s = select([users])
    result = connection.execute(s) 
    return(result)

def input_(input__: dict):
    global word_list
    word_list = input__
    return word_list
 
