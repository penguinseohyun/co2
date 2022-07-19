# 백준 11650번 좌표 정렬하기
import sys

def xy(arr):
    l = len(arr) # cnt와 같은 의미
    narr = sorted(arr)
    
    for i in range(l):
        print(narr[i][0], narr[i][1])




cnt = int(sys.stdin.readline())
arr = []
for i in range(cnt):
     num = list(map(int,sys.stdin.readline().split()))
     
     arr.append(num)

xy(arr)