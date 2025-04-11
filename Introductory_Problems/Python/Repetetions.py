def solution(n):
    ch = n[0]
    ans, cur = 0, 0

    l = len(n)
    for i in range(l):
        if n[i] == ch:
            cur = cur + 1
        else:
            cur = 1
        ch = n[i]
        ans = max(ans,cur)
    
    return ans

if __name__ == "__main__":
    n = input()
    print(solution(n), end = ' ')