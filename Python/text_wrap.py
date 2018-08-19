"""
Problem:
-----------
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Input Format:
------------
The first line contains a string, S.
The second line contains the width, w.

Output Format:
-------------
Print the text wrapped paragraph.
"""
import textwrap

def wrap(string, max_width):
    p = ""
    while len(string) >= max_width:
        p += string[0:max_width] + "\n"
        string = string[max_width:]
    p += string
    return p

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
