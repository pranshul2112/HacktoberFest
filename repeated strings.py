import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c=0
    for i in range(0,len(s)):
        if s[i]=="a":
            c=c+1
    sum=(n//len(s))*c
    r=n%len(s)
    for i in range(0,len(s)):
        if s[i]=="a":
            if i <r:
                sum+=1
    return (sum)
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
