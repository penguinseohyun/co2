#  백준 1181번 단어 정렬
import sys


cnt = int(sys.stdin.readline())
arr = []
for i in range(cnt):
    word = sys.stdin.readline().strip()
    if word not in arr:
        arr.append(word)
     
arr.sort()
arr.sort(key = lambda x:len(x)) # lambda람다 이용
for i in arr:
    print(i)