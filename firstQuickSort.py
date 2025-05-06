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
# Test the function
if __name__ == "__main__":
    sequence = [5, 2, 9, 1, 5, 6, 0, 2, 1 ,5, 6]
    print("Unsorted sequence:", sequence)
    sorted_sequence = quickSort(sequence)
    print("Sorted sequence:", sorted_sequence)