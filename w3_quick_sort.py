#First quick sort method
# Best case O(n log n)
# Worst case theta O(n^2) to avoid worse case, just randomize the pivot
# Average case O(n log n)


def quickSort(sequqence):
    length = len(sequqence)
    if length <= 1:
        return sequqence
    else:
        pivot = sequqence.pop()

    itemsGreater = []
    itemsLower = []

    for item in sequqence:
        if item > pivot:
            itemsGreater.append(item)
        else:
            itemsLower.append(item)
    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater) #repeat the process

#Aj. quicksort method
# [i] will point to the last element that less than or equal to the pivot
# [j] is the runner that will go through the array
def lomotoPartition(sequence, low, high):
    pivot = sequence[high]
    i = low - 1
    for j in range(low, high):
        if sequence[j] <= pivot:
            i += 1
            sequence[i], sequence[j] = sequence[j], sequence[i]
    sequence[i + 1], sequence[high] = sequence[high], sequence[i + 1]
    return i + 1

# [i] keep increasing until it finds an element that is greater than the pivot
# [j] keep decreasing until it finds an element that is less than the pivot
# [i] and [j] will swap the elements


def hoarePartition(sequence, low, high):
    pivot = sequence[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if sequence[j] < pivot:
            sequence[i], sequence[j] = sequence[j], sequence[i]
            i += 1
    sequence[low], sequence[i - 1] = sequence[i - 1], sequence[low]
    return i - 1

# Test the function
if __name__ == "__main__":
    sequence = [5, 2, 9, 1, 5, 6, 0, 2, 1 ,5, 6]
    print("Unsorted sequence:", sequence)
    sorted_sequence = quickSort(sequence)
    print("Sorted sequence:", sorted_sequence)