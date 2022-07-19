# 백준 2751번 수 정렬하기 2
# n개의 수 오름차순으로 정렬

def num(arr): #수 비교
    arr.sort()
        
# test count 받기
cnt = int(input())
arr = [0] * cnt # cnt만큼 배열 생성 및 초기화
#수 입력 받기
from sys import stdin
for i in range(cnt):
    arr[i] = int(stdin.readline())
    
num(arr)

#출력
answer = ""   
for i in arr:
    answer += (str(i) + '\n')
print(answer)