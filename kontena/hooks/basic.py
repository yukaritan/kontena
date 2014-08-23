from utils.hookutils import hook


@hook("(?P<thing1>.+)\s+(?P<isare>is|are)\s+(?P<thing2>.+)")
def test(match: dict):
    print("I have learned that {thing1} {isare} in fact {thing2}".format(**match))

