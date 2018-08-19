"""
Problem:
------------
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Input Format:
------------
A single line containing a string S.

Output Format:
-------------
Print the modified string S.

"""

def swap_case(s):
    nString = ''
    for c in s:
        if c.islower():
            nString += c.upper()
        elif c.isupper():
            nString += c.lower()
        else:
            nString += c
    return nString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
