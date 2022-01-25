#!/usr/bin/env python3

import sys
input = int(sys.argv[1])
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x !=0):
        return False
    else:
        reverse = 0
        while x > reverse:
            reverse = reverse*10 + x%10
            x = int(x/10)
            print(f"x={x}, reverse={reverse}")
        return int(x) == int(reverse) or int(x) == int(reverse/10)

if isPalindrome(input):
    print(f"yes {input} is a palindrome num")
else:
    print(f"{input} is not")
