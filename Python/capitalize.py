"""
Problem:
----------
You are asked to ensure that the first and last names of people begin with a
capital letter in their passports. For example, alison heck should be
apitalised correctly as Alison Heck.

alison heck => Alison Heck

Given a full name, your task is to capitalize the name appropriately.

Input Format:
------------
A single line of input containing the full name, .

Output Format:
-------------
Print the capitalized string, S.
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = list(s)
    prev = None
    for i,c in enumerate(l):
        if prev == None or prev == ' ':
            l[i] = c.capitalize()
        prev = c
    return ''.join(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
