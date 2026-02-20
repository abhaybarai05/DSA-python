"""
Day 1 - Python Fundamentals Practice
Topic: number_analysis

"""

def analyze_number(num):
    print("\n--- Number Analysis ---")
    
    # Even or Odd
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
    
    # Positive, Negative or Zero
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")
    
    # Divisible by 5 check
    if num % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is NOT divisible by 5.")


# Taking input from user
number = int(input("Enter a number: "))
analyze_number(number)


   
 