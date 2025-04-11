n = int(input())

sum = (n * (n+1)) // 2

l = list(map(int,input().split()))

for _ in range(len(l)):
    sum -= l[_]

print(sum)