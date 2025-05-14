def radix_sort(arr):
    # Separate integer and fractional parts
    # To handle floating points, we can convert them to integers by shifting the decimal place.
    if all(isinstance(x, float) for x in arr):  
        # If the list contains floating-point numbers
        # Find the maximum number of digits after the decimal point
        max_digits = max(len(str(abs(x)).split('.')[1]) if '.' in str(x) else 0 for x in arr)
        factor = 10 ** max_digits  # Multiply by this factor to convert floats to integers
        
        # Convert all numbers to integers
        arr = [int(x * factor) for x in arr]
    else:
        factor = 1  # If it's not floating-point, we just use 1
    
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    exp = 1  # Initialize exponent for the current digit

    # Perform counting sort for each digit
    while max_num // exp > 0:
        bucket_sort(arr, exp)
        exp *= 10  # Move to the next digit
    
    # If the numbers were originally floats, convert back to float
    if factor != 1:
        arr = [x / factor for x in arr]
    
    return arr

def bucket_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits (0-9)
    
    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the sorted numbers into the original array
    for i in range(n):
        arr[i] = output[i]