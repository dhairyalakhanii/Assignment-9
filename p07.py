def variance(numbers):
    mean_value = sum(numbers) / len(numbers)
    total=0
    for x in numbers:
        total += (x - mean_value) ** 2
    return total / len(numbers)
numbers = [5, 2, 8, 1, 9]
print("Variance:", variance(numbers))