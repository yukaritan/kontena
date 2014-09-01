#!/usr/bin/env python3

# we need to import the hooks we want to use
from hooks import basic
from utils.hookutils import *
from utils.dbutils import *
from utils.hookdbutils import *


class Kontena:
    def __init__(self):
        pass

    def handle_message(self, text: str):

        match_function_db = find_matching_function_db(text)
        match_function = find_matching_function(text)
        #sent_list = input_(text)
        #hook_db(text)
        if match_function:
            match, function = match_function
            hook_db(text)
            function(match)
        if match_function_db:
            mathcdb, functiondb = match_function_db
            dbhook(text)
            function(matchdb)


