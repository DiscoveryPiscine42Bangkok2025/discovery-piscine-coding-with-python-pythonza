#!/usr/bin/env python3

import sys

z = "z"

if(len(sys.argv) != 2 or not(z in sys.argv[1].lower())):
    print("none")
else:
    print(sys.argv[1].lower().count(z) * "z")