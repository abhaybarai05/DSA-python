def two_sum(arr, target):
    hashmap = {}  # value -> index

    for i in range(len(arr)):
        complement = target - arr[i]

        # Check if complement exists in hashmap
        if complement in hashmap:
            return [hashmap[complement], i]

        # Store current value with its index
        hashmap[arr[i]] = i

    return None


# Taking input
arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

result = two_sum(arr, target)

if result:
    print("Indices:", result)
else:
    print("No solution found")