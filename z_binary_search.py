def binary_search(list, target):
    first = 0               # O(1) #first position
    last = len(list) - 1    # O(1) #last  position

    while first <= last:
        midpoint = (first+last)//2      # O(1) #floor division

        if list[midpoint] == target:    # O(1) #best senerios
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1 

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

"""
O(log n)
"""