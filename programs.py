#check a no is prime
def is_prime(n): #The function is_prime(n) is defined to determine if a given number n is a prime number.
    '''The first condition if n <= 1: checks if the number is less than or equal to 1.If n is 1 or less, 
    the function immediately returns False because prime numbers are defined as greater than 1.'''
    if n <= 1:
        return False
    '''Iterate Over Possible Divisors:

    The for loop for i in range(2, n): iterates over all integers i starting from 2 up to n-1.
    This loop is used to check if n is divisible by any number other than 1 and itself.'''
    for i in range(2, n):
        '''Check for Divisibility:
        Inside the loop, the condition if n % i == 0: checks if n is divisible by i.
        The expression n % i calculates the remainder when n is divided by i.
        If the remainder is 0, it means n is divisible by i, indicating that n is not a prime number.'''
        if n % i == 0:
            '''If n is divisible by any i in the loop, the function returns False immediately, 
            indicating that n is not a prime number.'''
            return False
    '''If the loop completes without finding any divisors (i.e., n is not divisible by 
    any number from 2 to n-1),  the function returns True.
   This means n is a prime number because it has no divisors other than 1 and itself.'''

    return True
# Get input from the user
user_input = input("Enter a number: ")

# Convert the input to an integer
number = int(user_input)

# Check if the number is prime and print the result
result = is_prime(number)
print(result)

#divisible by 3
def is_divible(n):
    if n % 3 ==0:
        return True
    else:
       return False
user_input = input("enter a number : ")
number = int(user_input)
result = is_divible(number)
print(result)

#binary search
def binary_search_iterative(arr, target):
    # Define the search bounds
    left, right = 0, len(arr) - 1  
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2  
        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid  
        # If the target is bigger, narrow the search to the right half
        elif arr[mid] < target: 
            left = mid + 1  
        # If the target is smaller, narrow the search to the left half
        else: 
            right = mid - 1  
    # Return -1 if the target is not found
    return -1 

arr = [2, 3, 4, 10, 40]
target = 10

    
# Run the iterative function
result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Iterative: Target found at index {result}")
else:
    print("Iterative: Target not found")

#fibonachi nos 
def fibo(n):

    if n < 0:
        return "invalid fibo number"
    elif n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        lst = [1,1] # [1,1,2,3]
        for i in range(2,n):  # i = 2 , i =3
            lst.append(lst[i-2]+lst[i-1]) # lst[1],lst[2]
        return lst
print(fibo(20))            