from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt 

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))