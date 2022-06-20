#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    positive = 0
    negative = 0
    zero = 0
    
    ratio_positive = 0
    ratio_negative = 0
    ratio_zero = 0
    
    for i in range(len(arr)):
        
        if arr[i] < 0:
            negative+=1
            
        elif arr[i] == 0:
            zero+=1
            
        elif arr[i] > 0:
            positive+=1
            
    ratio_positive = positive/len(arr)
    ratio_negative = negative/len(arr)
    ratio_zero = zero/len(arr)
    
    print(ratio_positive)
    print(ratio_negative)
    print(ratio_zero)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
