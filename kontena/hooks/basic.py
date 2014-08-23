from utils.handlerutils import hook


@hook("(?P<thing1>.+)\s+is\s+(?P<thing2>.+)")
def test(match: dict):
    print("got", match)

