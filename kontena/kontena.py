#!/usr/bin/env python3

# we need to import the hooks we want to use
from hooks import basic
from utils.hookutils import find_matching_function


class Kontena:
    def __init__(self):
        pass

    def handle_message(self, text: str):

        match_function = find_matching_function(text)
        if match_function:
            match, function = match_function

            function(match)


