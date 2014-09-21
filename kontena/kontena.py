#!/usr/bin/env python3

# we need to import the hooks we want to use
#from hooks import basic
from hooks import basicdb
from hooks import basic
from utils.hookutils import *
from utils.dbutils import *
#from utils.hookdbutils import *


class Kontena:
    def __init__(self):
        pass

    def handle_message(self, text: str):

        match_function_db = find_matching_function_db(text)
        match_function = find_matching_function(text)

#        if match_function:
 #           match, function = match_function
  #          function(match)

        if match_function_db:
            x, functiondb = match_function_db
            functiondb(x)

        if match_function:
            match, function = match_function
            function(match)
