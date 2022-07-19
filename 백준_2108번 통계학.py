from collections import Counter
import sys

# 백준 2108번 통계학

# 산술 평균
def mathavr(arr, num):
    a = sum(arr)
    avr = float(a/ num)
    print(int(round(avr,0)))

# 중앙값
def middle(arr, num):
    narr = sorted(arr)
    num = int(num / 2)
    print(narr[num])

# 최빈값
def many(arr, num):
    arr = sorted(arr)
    narr = Counter(arr).most_common()
    if len(narr) > 1:
        if narr[0][1] == narr[1][1]:
            print(narr[1][0])
        else :
            print(narr[0][0])
    else:
        print(narr[0][0])

        
# 범위
def ran(arr, num):
    narr = sorted (arr)
    if narr[0] < 0:
        a = narr[0] * (-1) + narr[num-1]  
    else :
        a = narr[num-1] - narr[0]
    print(a)


num = int(sys.stdin.readline())
arr = []
for i in range(num):
    a = int(sys.stdin.readline())
    arr.append(a)

mathavr(arr,num)
middle(arr,num)
many(arr,num)
ran(arr,num)
