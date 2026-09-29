def standard_deviation(numbers):
    mean_value = sum(numbers) / len(numbers)
    total=0
    for x in numbers:
        total += (x - mean_value) ** 2
    variance = total / len(numbers)
    return variance ** 0.5
numbers = [5, 2, 8, 1, 9]
print("Standard Deviation:", standard_deviation(numbers))