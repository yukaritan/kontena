"""
The bot uses hooks and patterns to figure out what to do. Most of these are based on hooks found in Bucket.
http://wiki.xkcd.com/irc/Bucket#Teaching_factoids_to_Bucket
"""

from sqlalchemy.ext.declarative import declarative_base
from utils.hookutils import *
from sqlalchemy import *
import os

#if os.path.exists("info.db"):
#    pass
#else:
engine = create_engine('sqlite:///info.db', echo=False)

metadata = MetaData()


users = Table('users', metadata,
              Column("sentence",String),
        )


ins = users.insert()
conn = engine.connect()
Base = declarative_base()

#Base.metadata.create_all(engine)

#ins = users.insert().values(sentence="test")
#conn.execute(ins)

#
#  Teaching Kontena
#

@hook("(?P<person>.+?)<'s>\s+(?P<thing>.+)")
def belonging(match: dict):
#    global engine
#    global metadata
    
    """
    X<'s> Y
        After using this, if someone says "X", Bucket will respond "X's Y".
        Apostrophes - learn how to use them before using this.
    """
    global ins
    print("I have learned that {thing} belongs to {person}".format(**match))
    sentence_ = return_fn(text)
    ins = users.insert().values(sentence=sentence_)
    conn.execute(ins)


@hook("(?P<thing1>.+)\s+<action>\s+(?P<thing2>.+)")
def action(match: dict):
    """
    X <action> Y
        If you use "X <action> Y", when someone says "X", Bucket will use "/me Y".
        Like the above two types, retain the greater-than and lesser-than signs.
    """
    print("When someone says {thing1}, I will say /me {thing2}".format(**match))


@hook("(?P<thing1>.+)\s+<reply>\s+(?P<thing2>.+)")
def action(match: dict):
    """
    X <reply> Y
        You can say "X <reply> Y", when someone says "X", Bucket will respond "Y".
        You might see some people using "X is <reply> Y", this was formerly required so you may see older users use it.
    """
    print("When someone says {thing1}, I will reply with {thing2}".format(**match))


@hook("(?P<thing1>.+?)\s+<(?P<verb>.+)>\s+(?P<thing2>.+)")
def verb(match: dict):
    """
    X <verb> Y
        You can use other things instead of "is" or "are" by putting them inside greater and lesser-than signs, such as "X <hates> Y" or "X <compliments> Y"
    """
    print("I have learned that {thing1} {verb} {thing2}".format(**match))


@hook("(?P<thing1>.+?)\s+(?P<auxiliary_verb>is|are)\s+(?P<thing2>.+)")
def auxiliary_verb(match: dict):
    """
    X is Y
        The most common type of factoid you can teach to Bucket is by simply saying "X is Y".
        If someone says "X" later on, Bucket will reply "X is Y"

        Be careful about accidentally creating a new factoid while talking to Bucket.
        You can also say "X is also Y", this was formerly required to attach multiple factoids to one trigger so you
        may see older users use this.
        If you type "X is Y is Z", Bucket will split it on the first "is", making the trigger "X" and
        the factoid "Y is Z" and Bucket will respond "X is Y is Z".

        If you wanted 'X is Y' to trigger 'Z', teach Bucket 'X is Y <is> Z'. See <verb> below.

    X are Y
        Similar to "X is Y", you can teach this kind of factoid by simply saying "X are Y" and if someone says X later on, Bucket will reply "X are Y"
    """
    print("I have learned that {thing1} {auxiliary_verb} in fact {thing2}".format(**match))
