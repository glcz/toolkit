#!/usr/bin/env python
import random

larousse = {
    1: "token",
    2: "cat",
    3: "dog",
    4: "foo",
    5: "pocket",
    6: "mother",
    7: "father",
    8: "brother",
    9: "eyes",
    10: "hands",
    11: "fat",
    12: "gnoll",
    13: "wizard",
    14: "metro",
    15: "cyber",
    16: "shake",
    17: "hand",
    18: "sorcerer",
    19: "pangea",
    20: "crusader",
    21: "kangaroo",
    22: "shack",
    23: "snow",
    24: "net",
    25: "gnome",
    26: "human",
    27: "lizard",
    28: "soup",
    29: "mushroom",
    30: "beef",
    31: "satellite",
    32: "cheese",
    33: "moldy",
    34: "water",
    35: "mud",
    36: "dust",
    37: "point",
    38: "points",
    39: "contra",
    40: "fever",
}

lastkey = max(larousse.keys())
nbpossibles = max(larousse.keys()) * max(larousse.keys())

prefixe1 = random.randint(1,lastkey)
suffixe1 = random.randint(1,lastkey)
username1 = larousse[prefixe1].capitalize() + larousse[suffixe1].capitalize()

prefixe2 = random.randint(1,lastkey)
suffixe2 = random.randint(1,lastkey)
username2 = larousse[prefixe2].capitalize() + larousse[suffixe2].capitalize()

prefixe3 = random.randint(1,lastkey)
suffixe3 = random.randint(1,lastkey)
username3 = larousse[prefixe3].capitalize() + larousse[suffixe3].capitalize()


print(f"{username1} // {username2} // {username3}")
print(f"Choisis parmi {nbpossibles} possibilités")