#https://www.codechef.com/ZCOPRAC/problems/ZCO14001

import sys
input=sys.stdin.readline

n, h = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

pointer = 0
status = 0

for query in queries:
    if query == 1 and pointer > 0:
        pointer -= 1
    elif query == 2 and pointer < n - 1:
        pointer += 1
    elif query == 3 and status == 0 and arr[pointer] > 0:
        status = 1
        arr[pointer] -= 1
    elif query == 4 and status == 1 and arr[pointer] < h:
        status = 0
        arr[pointer] += 1
    elif query == 0:
        break

print(*arr)