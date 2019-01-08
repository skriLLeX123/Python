# program to catch error and print it
n=int(input())
for i in range(n):
    try:
        x,y=map(int,input().split())
        print(x//y)
    except Exception as e:
        print("Error Code:",e)

