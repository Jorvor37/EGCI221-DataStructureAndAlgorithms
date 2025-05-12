def recursive_binary_search(list, target):
    if len(list) == 0:                  # O(1)
        return False                    # O(1)
    else:
        midpoint = (len(list))//2       # O(1)

        if list[midpoint] == target:    # O(1)
            return True                 # O(1)
        else:                           # the different
            if list[midpoint] < target:     #create sublist
                return recursive_binary_search(list[midpoint+1:], target)   # O(n) #goes to the end
            else:
                return recursive_binary_search(list[:midpoint], target)     # O(n) #goes from the start to the end

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)