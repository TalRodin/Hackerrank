#!/bin/python3

N = int(input())
if N%2!=0:
    print ('Weird')
else:
    if 2<=N<=5:
        print('Not Weird')
    if 6<=N<=20:
        print ('Weird')
    if N>20:
        print('Not Weird')
