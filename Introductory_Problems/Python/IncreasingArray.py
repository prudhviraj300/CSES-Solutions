def sol(n, l):
    ops = 0
    for i in range(1,n):
        if l[i] < l[i-1]:
            ops = ops + (l[i-1] - l[i])
            l[i] = l[i-1]
    return ops

if __name__ == "__main__":
    n = int(input())
    l = list(map(int,input().split()))
    print(sol(n, l))
