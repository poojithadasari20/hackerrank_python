#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:]=="AM":
        if s[:2]=="12":
            return ("00"+s[2:8])
        else:
            return s[:8]
    else:
        if s[:2]=="12":
            return s[:8]
        else:
            return (str(int(s[:2])
            +12)+s[2:8])                                    
s = input()
print(timeConversion(s))


