# 백준 10989번 수 정렬하기 3
# 메모리 초과 오류 뜸 해결방법 모르겠습니다..

import sys
        
cnt = int(input())
arr = [0] * 10001 

li = []
for i in range(cnt):
    a = int(sys.stdin.readline())
    li.append(a)
   
li.sort(key = lambda x : x)

for i in li:
    print(i)