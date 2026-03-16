def reverse_array(arr):
    left = 0                   
    right = len(arr) - 1        

    while left < right:         
        arr[left], arr[right] = arr[right], arr[left]  

        left += 1              
        right -= 1             



arr = list(map(int, input("Enter numbers separated by space: ").split()))

reverse_array(arr)              

print("Reversed array:", arr)   