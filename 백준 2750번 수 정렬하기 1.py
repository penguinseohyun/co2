# 백준 2750번 수 정렬하기 1
# n개의 수 오름차순으로 정렬

def num(list): #수 비교
    list.sort()
        
# test count 받기
cnt = int(input())
list = []
#수 입력 받기-> 수 비교하기
for i in range(cnt):
    a = int(input())
    list.append(a)
    
num(list)

#출력   
for i in range(cnt):
    print(list[i])