from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.sql import *
import os
from collections import *
import re
import sys


triggers = OrderedDict()

db_list = []
word_list=[]


engine = create_engine('sqlite:///logs.db', echo=False)

connection =engine.connect()

metadata = MetaData(engine)

facts = Table('facts', metadata,
        Column('facts', String()),
     
)

every = Table('every',metadata,
        Column('every',String())
)

try:
    #connection.execute(
    #"""
    #CREATE TABLE users (
    #    triggers VARCHAR
    #);
    #"""
    #)

    metadata.create_all(engine) 

    
except:
    pass

#users = Table('users', metadata, Column('triggers', String()))


def insert_db(text,which="triggers"):

    global facts
    if which != "facts":

        ins = facts.insert().values(facts=text)
        connection.execute(ins)
        
    elif which == "facts":

        connection.execute(
        """                                                                                         
        
        INSERT INTO every (every) VALUES (?);                                                    
        """,
        text
        )


#def output_db():
    
#    global connection
#    global users
#    s = select([users])
#    result = connection.execute(s) 
#    return(result)

def lookfor(pattern):
    Found_=False
    end=False
    Found=False
    liste_=[]
    s = select([every.c.every])
    result=connection.execute(s)
    
    for i in result:
        liste_.append(i)


    while Found_==False:
        
        for item in liste_:
            
            item_=str(item[0])
            #print(item_)
            if pattern.match(item_):
                #print("JA!")
                Found_ = True
                print(item_)
                #sys.exit(0)
                break
            
        return

                
                
            #if Found_ != True:
            #    print("I will not add  test")
            #Found_=True
            #else:
            #    print("I will add test")
            #break
