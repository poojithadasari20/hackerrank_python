#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):

    apples_count=0
    oranges_count=0
    for i in apples:
        if s<= a + i <=t:
            apples_count+=1
    for j in oranges:
        if s<= b + j <= t:
            oranges_count+=1
    print(apples_count)
    print(oranges_count)      

if __name__ == '__main__':
    
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())

    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    
    
    
    
    
