#!/usr/bin/env python3

# we need to import the hooks we want to use
from hooks import basic
from utils.hookutils import *
from utils.dbutils import *


class Kontena:
    def __init__(self):
        pass

    def handle_message(self, text: str):

        match_function = find_matching_function(text)
        #sent_list = input_(text)
        hook_db(text)
        if match_function:
            match, function = match_function

            function(match)


