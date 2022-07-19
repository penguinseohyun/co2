# 백준_1427번 소트인사이드

def down(a):
    arr = []
    for i in str(a):
        arr.append(int(i))

    print(arr)
    arr.sort(reverse = True)
    

    for i in arr:
        print(i,end='')
        
a = int(input())
down(a)