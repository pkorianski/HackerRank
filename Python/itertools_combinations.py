"""
Problem:
-----------
You are given a string S. Your task is to print all possible combinations, up
to size k, of the string in lexicographic sorted order.

Input Format:
------------
A single line containing the string S and integer value k separated by a space.

Output Format:
-------------
Print the different combinations of string S on separate lines.
"""

from itertools import combinations

ui = input().split()
l = list(ui[0])
l.sort()
l = ''.join(l)
result = []
k = None
if len(ui) == 2:
    k = int(ui[1])
for n in range(1,k+1):
    com = list(combinations(l,n))
    com.sort()
    result.extend(com)
for i,v in enumerate(result):
    print(''.join(v))
