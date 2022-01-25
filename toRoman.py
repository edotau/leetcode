#!/usr/bin/env python3

class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        dictionary = {1:"I", 4: "IV", 5:"V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100:"C", 400: "CD", 500:"D", 900: "CM", 1000:"M"}
        max_table = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        while num > 0:
            if num >=max_table[0]:
                ans = ans + dictionary[max_table[0]]

                num-= max_table[0]
            for key in range(0, len(max_table)):
                while max_table[key] <= num:
                    ans += dictionary[max_table[key]]
                    num-=max_table[key]
        return ans


inputs = [20, 58, 500, 1994, 1476]

outputs = ["XX", "LVIII", "D", "MCMXCIV", "MCDLXXVI"]

for i in range(0, len(inputs)):
    t = Solution()
    ans = t.intToRoman(inputs[i])
    print(f"{ans}")
    if ans != outputs[i]:
        print("Error: Need to debug...")

# "MCMXCIV"]