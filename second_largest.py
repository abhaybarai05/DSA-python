def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second


arr = list(map(int, input("Enter numbers separated by space: ").split()))
result = second_largest(arr)

if result is None:
    print("No second largest number found.")
else:
    print("The second largest number is:", result)