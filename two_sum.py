def two_sum(arr, target):
    hashmap = {}  

    for i in range(len(arr)):
        complement = target - arr[i]

        
        if complement in hashmap:
            return [hashmap[complement], i]

       
        hashmap[arr[i]] = i

    return None



arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

result = two_sum(arr, target)

if result:
    print("Indices:", result)
else:
    print("No solution found")