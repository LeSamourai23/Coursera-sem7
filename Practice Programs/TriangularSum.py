def TSum(n):
    if n==0:
        return 0

    return n + TSum(n-1)

print(TSum(5))