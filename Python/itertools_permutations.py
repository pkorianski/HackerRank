"""
Problem:
-----------
You are given a string S. Your task is to print all possible permutations of
size k of the string in lexicographic sorted order.

Input Format:
------------
A single line containing the space separated string S and the integer value k.

Output Format:
-------------
Print the permutations of the string S on separate lines.
"""
from itertools import permutations

l = input().split()
s = list(l[0])
k = None
if len(l) == 2:
    k = int(l[1])
result = ""
perm = list(permutations(s,k))
perm.sort()
for i,t in enumerate(perm):
    if i != len(perm)-1: result += ''.join(t) + '\n'
    else: result += ''.join(t)
print(result)
