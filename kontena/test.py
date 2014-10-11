from kontena import Kontena
from utils.dbutils import *

kontena = Kontena()

tests = ["no","x is y"]


for test in tests:
    kontena.handle_message(test)

while True:
    a = input("Questions?: ")

    kontena.handle_message(a)

