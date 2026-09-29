def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]
def variance(numbers):
    mean_value = sum(numbers) / len(numbers)
    total=0
    for x in numbers:
        total += (x - mean_value) ** 2
    return total / len(numbers)
def standard_deviation(numbers):
    mean_value = sum(numbers) / len(numbers)
    total=0
    for x in numbers:
        total += (x - mean_value) ** 2
    variance = total / len(numbers)
    return variance ** 0.5
def quartile(numbers):
    numbers.sort()
    n = len(numbers)
    q1 = median(numbers[:n // 2])
    q3 = median(numbers[(n + 1) // 2:])
    return q1, q3
n=int(input("Enter the number of students: "))
marks=[]
for i in range(n):
    mark=int(input(f"Enter the marks of student {i+1}: "))
    marks.append(mark)
print("\nAll marks:", marks)
total_marks = sum(marks)
print("Total marks:", total_marks)
mean_marks = total_marks / n
print("Mean marks:", mean_marks)
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Median marks:", median(marks))
print("Variance of marks:", variance(marks))
print("Standard Deviation of marks:", standard_deviation(marks))
q1,q3=quartile(marks)
print("First Quartile (Q1):", q1)
print("Second Quartile (Q2):", median(marks))
print("Third Quartile (Q3):", q3)
pass_count=0
fail_count=0
for mark in marks:
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)
print("Sorted marks:", sorted(marks))