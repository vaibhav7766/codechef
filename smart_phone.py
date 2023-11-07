#https://www.codechef.com/ZCOPRAC/problems/ZCO14003

# cook your dish here
import sys
input=sys.stdin.readline

n = int(input())
arr = sorted(int(input()) for _ in range(n))
max_revenue = max(arr[i] * (n - i) for i in range(n))
print(max_revenue)