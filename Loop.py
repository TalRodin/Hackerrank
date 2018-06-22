#!/bin/python3

import math
import os
import random
import re
import sys

def calc_(n):
    for i in range(1,10+1):
        print(n,'x',i,'=',n*i)
        
if __name__ == '__main__':
    n = int(input())
    calc_(n)
