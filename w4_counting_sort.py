"""
counting sort is stable

1. count all elements on index and store in C array (ex. 2 of 1, 0 of 2, 3 of 3)
2. count the sum
3. use that counted number to create new index by
4. check which number appear from bottom to front
5. and put select number to position of c

If I move pointer from array a from right to left what if left to right is it unstable sort. If I change a little bit on algorithm what it's gonna looks like
"""

def counting_sort(array):
    M = max(array)

    count_array = [0] * (M + 1)

    # Mapping each element of array as an index of count_array
    for num in array:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    output_array = [0] * len(array)

    for i in range(len(array) - 1, -1, -1):
        output_array[count_array[array[i]] - 1] = array[i]
        count_array[array[i]] -= 1

    return output_array

# Driver code
if __name__ == "__main__":
    # Input array
    array = [4, 3, 12, 1, 5, 5, 3, 9]

    # Output array
    output_array = counting_sort(array)

    for num in output_array:
        print(num, end=" ")