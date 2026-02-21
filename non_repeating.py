def first_non_repeating(arr):
    frequency = {}

    # Count frequency of each element
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find first element with frequency 1
    for num in arr:
        if frequency[num] == 1:
            return num

    return None


arr = list(map(int, input("Enter numbers separated by space: ").split()))
result = first_non_repeating(arr)

if result is None:
    print("No non-repeating element found.")
else:
    print("First non-repeating element is:", result)