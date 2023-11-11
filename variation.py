#https://www.codechef.com/ZCOPRAC/problems/ZCO15002

# cook your dish here
import sys
input=sys.stdin.readline

def total_variation_count(n, arr, K):
    arr.sort()
    count = 0

    i, j = 0, 1

    while j < n:
        if arr[j] - arr[i] >= K:
            count += n - j
            i += 1
        else:
            j += 1

    return count
    
n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(total_variation_count(n,arr,k))