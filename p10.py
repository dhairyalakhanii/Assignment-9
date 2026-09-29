def mean_absolute_deviation(numbers):
    mean_value = sum(numbers) / len(numbers)
    total=0
    for x in numbers:
        total += abs(x - mean_value)
    return total / len(numbers)
numbers = [5, 2, 8, 1, 9]
print("Mean Absolute Deviation:", mean_absolute_deviation(numbers))