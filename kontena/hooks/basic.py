from utils.hookutils import hook


@hook("(?P<thing1>.+)\s+(?P<auxiliary_verb>is|are)\s+(?P<thing2>.+)")
def test(match: dict):
    print("I have learned that {thing1} {auxiliary_verb} in fact {thing2}".format(**match))

