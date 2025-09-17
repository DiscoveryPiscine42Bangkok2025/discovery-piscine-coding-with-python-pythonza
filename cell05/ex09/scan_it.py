#!/usr/bin/env python3

import sys
import re

if(len(sys.argv) != 3 or len(re.findall(sys.argv[1], sys.argv[2])) == 0):
    print("none")
else:
    print(len(re.findall(sys.argv[1], sys.argv[2])))