from kontena import Kontena
from utils.dbutils import *

kontena = Kontena()

tests = ["no"]


for test in tests:
    kontena.handle_message(test)



