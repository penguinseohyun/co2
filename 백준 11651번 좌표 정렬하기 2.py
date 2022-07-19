# 백준 11651번 좌표 정렬하기 2
import sys

def xy(arr):
    l = len(arr) # cnt와 같은 의미
    narr = sorted(arr)
    
    for i in range(l):
        print(narr[i][1], narr[i][0])




cnt = int(sys.stdin.readline())
arr = []
for i in range(cnt):
     x,y = list(map(int,sys.stdin.readline().split()))
     
     arr.append((y,x))

xy(arr)