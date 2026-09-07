#selection sort for a list of numbers
numbers = [64, 25, 12, 22, 11]
def sel_sort(numbers):
    n = len(numbers)
    for i in range(0,n - 1):
        smallest = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[smallest]:
                smallest = j
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    return numbers
print("The unsorted list is ",numbers)
print("The sorted list is",sel_sort(numbers))
