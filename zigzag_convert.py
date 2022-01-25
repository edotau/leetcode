#!/usr/bin/env python3
import sys

intputString = str(sys.argv[1])
rows =  int(sys.argv[2])

def convert(s:str, numRows:int) ->str:
    if numRows == 1:
        return s
    ans = ""
    n = int(len(s))
    cycle = 2 * numRows - 2

    for i in range(0, numRows):
        j = 0
        while i+j < n:
            ans+= s[i+j]
            if i != 0 and i != numRows -1 and j+cycle-i < n:
                ans +=s[j+cycle-i]
            j+=cycle
    return ans

print(f"ans={convert(intputString, rows)}")