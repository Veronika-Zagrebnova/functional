def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

print(climb_stairs(13))  