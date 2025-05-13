def linear_search(list, target):
    """
    Return the index position of the target if found, else return none\
    """

    for i in range(0, len(list)):   #O(n)
        if list[i] == target:       #O(n)
            return i                #O(1)
    return None                     #O(1)

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)