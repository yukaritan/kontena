from kontena import Kontena
from utils.dbutils import *

kontena = Kontena()

tests = ["X is Y",
         "X are Y",
         "X<'s> Y",
         "X <reply> Y",
         "X <action> Y"]


for test in tests:
    kontena.handle_message(test)



