#!/usr/bin/env python3

import sys
sys.path.append('.')

# we need to import the handlers we want to use
from handlers import basic
from utils.handlerutils import find_matching_function


class Kontena:
    def __init__(self):
        pass

    def handle_message(self, text: str):

        match_function = find_matching_function(text)
        if match_function:
            match, function = match_function

            function(match)


Kontena().handle_message("a is b")
Kontena().handle_message("dog is cat")
Kontena().handle_message("human watches football")  # no match for this line
