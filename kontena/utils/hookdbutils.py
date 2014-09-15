from collections import OrderedDict
import re

triggers = OrderedDict()


def dbhook(regex: str):

    """This is used to bind a function to a regex pattern"""

    def wrapper(fn):
        triggers[re.compile(regex, re.IGNORECASE)] = fn
        return fn

    return wrapper


def cmdhook(regex: str):

    """The same as a hook, but it must begin with a certain prefix"""

    regex = ";;" + regex

    def wrapper(fn):
        triggers[re.compile(regex, re.IGNORECASE)] = fn
        return fn

    return wrapper


def find_matching_function_db(text: str) -> (dict, callable):

    """Matchest a given string against known triggers, stops on the first positive result"""
    
    
    # this calls find_matching_functions and returns only the first match
    for match, function in find_matching_functions_db(text):
        return match, function


def find_matching_functions_db(text: str) -> (dict, callable):

    """Matchest a given string against known triggers, tries to find as many results as possible"""

    for trigger, function in triggers.items():
        match = trigger.match(text)
        if match:
            yield match.groupdict(), function

def return_fn(text:str):
    return text
