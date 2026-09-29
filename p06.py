def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]
numbers = [5, 2, 8, 1, 9]
print("Median:", median(numbers))