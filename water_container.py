#!/usr/bin/env python3


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            max_area = max(min(height[right], height[left])*(right-left), max_area)
            if height[right] < height[left]:
                right-=1
            else:
                left+=1
        return max_area




# Testing data:
inputs = [[1,1], [1,8]]

outputs = [1,8]

for each in range(0, len(inputs)):
    t = Solution()
    if t.maxArea(inputs[each]) != outputs[each]:
        (f"Error: {t.maxArea(inputs[each])} does not equal {outputs[each]}")

print("Yay, you got it to work...")

