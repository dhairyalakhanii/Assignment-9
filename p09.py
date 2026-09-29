from statistics import median
def quartiles(numbers):
    numbers.sort()
    n = len(numbers)
    q2 = median(numbers)
    if n % 2 == 0:
        lower_half = numbers[:n // 2]
        upper_half = numbers[n // 2:]
    else:
        lower_half = numbers[:n // 2]
        upper_half = numbers[n // 2 + 1:]
    q1 = median(lower_half)
    q3 = median(upper_half)
    return q1, q2, q3
numbers = [5, 2, 8, 1, 9]
q1, q2, q3 = quartiles(numbers)
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)