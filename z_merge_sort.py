def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide : Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the soreted sublists created in previos step

    Takes O(n log n) times
        - O(n) from merge
        - O(log n) from split

    Takes n size of space
    """

    #stopping condition
    if len(list) <= 1:
        return list
    
    #Divide
    left_half, right_half = split(list)

    #Conquer
    left  = merge_sort(left_half)
    right = merge_sort(right_half)

    #Combine
    return merge(left,  right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(log n)
    """

    
    mid     = len(list)//2 #this will takes O(k)
    left    = list[:mid] #start to midpoint, not include midpoint
    right   = list[mid:] #midpoint to start, include midpoint

    #so the actual time should be O(k log n)

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    Takes overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    #right list is shorter than the left
    while i < len(left):
        l.append(left[i])
        i += 1

    #left list is shorter than the right
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])



alist = [54,26, 62, 93, 17, 77, 31, 44, 55, 20]

print(verify_sorted(alist))
l = merge_sort(alist)
print(l)
print(verify_sorted(l))
