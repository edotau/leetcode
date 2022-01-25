#!/usr/bin/env python3

def atoi(input):
    sign = 1
    ans = 0
    idx = 0
    n = len(input)

    intmax = pow(2,31)-1
    intmin = -pow(2,31)


    while idx < n and str(input[idx]) == ' ':
        idx+=1

    if idx < n and input[idx] == '+':
        sign = 1
        idx+=1
    elif idx < n and input[idx] == '-':
        sign = -1
        idx+=1

    while idx < n and input[idx].isdigit():
        digit = int(input[idx])
        print(f"digit={digit}")
        # Check overflow and underflow conditions.
        if ((ans > intmax // 10) or (ans == intmax // 10 and digit > intmax % 10)):
            # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
            return intmax if sign == 1 else intmin

        ans = 10 * ans + digit
        idx+= 1

    return sign * ans

query = ["4193 with words",  "42", "   -42", "+-12"]
ans = [4193, 42, -42, -12]
print(f"Running tests on {query}")
for i in range(0, len(query)):
    if not atoi(query[i]) == ans[i]:
        print(f"Error: there is s bug in your code...")

    print("It works!!!!!")