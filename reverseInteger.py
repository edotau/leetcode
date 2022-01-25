#!/usr/bin/env python3

import sys
input = int(sys.argv[1])

def wraper(x):
    if x < 0:
        ans = reverse(x*-1)
        return ans*-1
    else:
        return reverse(x)

def reverse(x):
    if x < 0:
        abs = -1
        x = x*-1
    else:
        abs = 1

    maxint = pow(2,31)-1
    minint =  maxint*-1-1
    rev = int(0)
    while x != 0:
        pop = int(x%10)
        x = int(x/10)
        if rev > int(maxint/10) or rev == int(maxint/10) and pop > 7:
            return 0
        if rev < int(minint/10) or rev == int(minint/10) and pop < -8:
            return 0
        rev = int(rev*10 + pop)
        print(f"rev={rev}, x={x}")
    return abs*rev

print(f"reverse of {input} is FINAL:{reverse(input)}")
