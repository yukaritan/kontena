#from hooks.basic import *
from sqlalchemy import *
from sqlalchemy.engine import *
import os

db_list = []
word_list=[]

if os.path.exists(""):
    pass
else:
    engine = create_engine('sqlite:///logs.db', echo=False)

connection = engine.connect()

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
    return db_list[0]



def input_(input__: dict):
    global word_list
    word_list = input__
    return word_list
