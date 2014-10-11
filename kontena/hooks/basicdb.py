"""
The bot uses hooks and patterns to figure out what to do. Most of these are based on hooks found in Bucket.
http://wiki.xkcd.com/irc/Bucket#Teaching_factoids_to_Bucket
"""

from utils.hookdbutils import *

#
#  Teaching Kontena
#



@hook_db("what is (?P<thing>.+)")
def belonging(match: dict):
    
    """
    what belongs to  <thing>?
        After using this, Kontena will tell you what belongs to thing.
    """
    #testlist = []
    #test1,test2=output_db()
    #print(test)
    #for row in test1:
    #    testlist.append(str(row))
    answer = re.compile(match["thing"]+" is\s+(?P<y>.+)")
    print(match["thing"])
    lookfor(answer)

    

