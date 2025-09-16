#!/usr/bin/env python3
i = 0
j = 0
while(i < 11):
    print(f"teble de {i}:", end = " ")
    j = 0
    while(j < 11):
        print(i * j, end = " ")
        j=j+1
    print("")
    i=i+1