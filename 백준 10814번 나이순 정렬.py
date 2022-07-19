# 백준 10814번 나이순 정렬
import sys

cnt = int(sys.stdin.readline())
li = []

for i in range(cnt):
    age,name = list(map(str, sys.stdin.readline().split()))
    age = int(age) # Q. 이게 없으면 왜 틀리나요 결과값은 잘 출력되는데...
    li.append((age,name))

li.sort(key = lambda x : x[0])

for i in li:
    print(i[0], i[1])