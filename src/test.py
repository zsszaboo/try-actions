from pathlib import Path
from random import randint

abc = " abc def ghijkl mno pqrs tu vwxyz"

with open("./result/random.txt", "w") as msg:
    for i in range(10):
        message = ""
        for i in range(160):
            message += abc[ randint(0, len(abc)-1 ) ]
        msg.write(message + "\n")
