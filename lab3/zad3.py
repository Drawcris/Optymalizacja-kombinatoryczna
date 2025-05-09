from time import perf_counter
from functools import lru_cache


def calculate_time_for_function(func, arg):
    start_time = perf_counter()
    print(f"Maksymalna liczba punktów: {func(arg)}")
    end_time = perf_counter()
    actual_time = end_time - start_time
    if actual_time < 1e-3:
        return f"Wykonano w {actual_time * 1_000_000:.2f} mikrosekund"
    elif actual_time < 1:
        return f"Wykonano w {actual_time * 1000:.2f} milisekund"
    else:
        return f"Wykonano w {actual_time:.2f} sekund"


def max_score(arr):
    if not (2 <= len(arr) <= 200):
        raise ValueError("Długość ciągu musi zawierać się w przedziale [2, 200].")
    if not all(1 <= x <= 100 for x in arr):
        raise ValueError("Wszystkie elementy muszą zawierać się w przedziale [1, 100].")

    n = len(arr)

    @lru_cache(maxsize=None)
    def dp(i, j):
        if j - i <= 1:
            return 0
        best = 0
        for k in range(i + 1, j):
            score = arr[i] + arr[k] + arr[j]
            total = dp(i, k) + dp(k, j) + score
            best = max(best, total)
        return best

    return dp(0, n - 1)

arr = [2, 1, 5, 1, 4]

print(calculate_time_for_function(max_score, arr))
