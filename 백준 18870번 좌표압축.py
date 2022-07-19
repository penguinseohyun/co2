# 백준 18870번 좌표압축
import sys

cnt = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split())) # 입력 데이터
n = sorted(set(num)) # 중복제거하고 오름차순 정리

dic = {}
a = 0

for i in n:
    dic[i] = a
    a += 1

result = []
for i in num:
    if i in dic:
        i = dic[i]
        result.append(i)

for i in result:
    print(i,"" ,end='')