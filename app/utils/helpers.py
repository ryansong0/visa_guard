def clamp_score(n: int, minnum: int, maxnum: int) -> int:
    return max(min(maxnum, n), minnum)