#!/usr/bin/env python3


def longestCommonPrefix(strs):
  if len(strs) == 0:
    return ""
  if len(strs) == 1:
    return strs[0]

  min_len = len(strs[0])
  for i in range(1, len(strs)):
    min_len = min( min_len, len(strs[i]))

  low_idx = 1
  high_idx = min_len
  while low_idx <= high_idx:
    mid_idx = (low_idx + high_idx) / 2
    if findCommon(strs, mid_idx):
      low_idx = mid_idx + 1
    else:
      high_idx = mid_idx - 1
    return  strs[0][0:int((low_idx+high_idx)/2)]

def findCommon(words, min_len):
  prefix = ""
  for i in range(0, len(words)):
    tmp = words[]
  for i in range(1, len(words)):
    if words[i] != query:
      return False
  return True

def longestPrefix(strs):
  if len(strs)==0:
    return ""
  if len(strs)==1:
    return strs[0]
  cp = ''
  l = [len(st) for st in strs] #lengths for each string
  for i in range(min(l)): # scan from first letter to min str lengths
    tmp = [s[i] for s in strs] #get i-th letter from each string
    if min(tmp)==max(tmp): #check if all of them are the same
      cp = cp + tmp[0]
    else:
      return cp
  return cp

words = ["flower","flow","flight"]

ans = longestPrefix(words)

print(f"the longest common prefix is: {ans}")