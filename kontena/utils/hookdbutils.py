from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.sql import *
import os
from collections import *
import re
from utils.dbutils import *


triggers = OrderedDict()

db_list = []
word_list=[]


engine = create_engine('sqlite:///logs.db', echo=False)

connection = engine.connect()

metadata = MetaData(engine)

users = Table('users', metadata, Column('sentence', String()))


def hook_db(regex:str):
    
    """Used to save what was said"""

    global db_list
    global word_list
    
    db_list.append(text)
    
    insert_db(regex)
    

    def wrapper(fn):
        triggers[re.compile(regex,re.IGNORECASE)]=fn
        return fn

    return  wrapper


def input_(input__: dict):
    global word_list
    word_list = input__
    return word_list
 
def find_matching_function_db(text: str) -> (dict, callable):

    """Matchest a given string against known triggers, stops on the\
    first positive result"""


    for match, function in find_matching_functions_db(text):
        return match, function


def find_matching_functions_db(text: str) -> (dict, callable):

    """Matchest a given string against known triggers, tries to find \
as many results as possible"""

    for trigger, function in triggers.items():
        match = trigger.match(text)
        if match:
            yield match.groupdict(), function

def return_fn(text:str):
    return text



