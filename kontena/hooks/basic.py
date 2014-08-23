from utils.hookutils import hook


@hook("(?P<thing1>.+?)\s+(?P<auxiliary_verb>is|are)\s+(?P<thing2>.+)")
def auxiliary_verb(match: dict):
    print("I have learned that {thing1} {auxiliary_verb} in fact {thing2}".format(**match))


@hook("(?P<person>.+?)<'s>\s+(?P<thing>.+)")
def belonging(match: dict):
    print("I have learned that {thing} belongs to {person}".format(**match))


@hook("(?P<thing1>.+)\s+<action>\s+(?P<thing2>.+)")
def action(match: dict):
    print("When someone says {thing1}, I will say /me {thing2}".format(**match))


@hook("(?P<thing1>.+)\s+<reply>\s+(?P<thing2>.+)")
def action(match: dict):
    print("When someone says {thing1}, I will reply with {thing2}".format(**match))


@hook("(?P<thing1>.+?)\s+<(?P<verb>.+)>\s+(?P<thing2>.+)")
def verb(match: dict):
    print("I have learned that {thing1} {verb} {thing2}".format(**match))
