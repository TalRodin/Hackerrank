#!/bin/python3

import math
import os
import random
import re
import sys

def sorted_(arr, k):
    for i in sorted(arr, key=lambda x : x[k]):
        
        print (*i)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    sorted_(arr, k)

