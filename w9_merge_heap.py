def heapify(arr, n, i):     #change "def" to "procedure", change "=" to ":="
    """
    Maintain the heap property by ensuring that the subtree rooted at index i is a valid min-heap.
    """
    smallest = i    ### largest = i
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index
    # If left child exists and is smaller than the smallest
    if left < n and arr[left] < arr[smallest]:      ### if left < n and arr[left] > arr[largest]:
        smallest = left                             ### largest = left
    # If right child exists and is smaller than the smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    # If smallest is not the current node, swap and heapify the affected subtree
    if smallest != i:                               ###change all smallest to largest
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)
def merge_heaps(heap1, heap2):
    # Step 1: Combine both heaps
    combined = heap1 + heap2
    # Step 2: Build the heap by heapifying from the last non-leaf node
    n = len(combined)
    start_index = (n // 2) - 1  # Last non-leaf node index
    # Step 3: Perform heapify operation from bottom to top
    for i in range(start_index, -1, -1):
        heapify(combined, n, i)
    return combined


def heapify_max(arr, n, i):
    """
    Maintain the heap property for a max-heap by ensuring that the subtree rooted at index i is a valid max-heap.
    """
    largest = i  # Assume the current node is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is larger than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the current node, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_max(arr, n, largest)


def merge_max_heaps(heap1, heap2):
    # Step 1: Combine both heaps
    combined = heap1 + heap2

    # Step 2: Build the max-heap by heapifying from the last non-leaf node
    n = len(combined)
    start_index = (n // 2) - 1  # Last non-leaf node index

    # Step 3: Perform heapify operation from bottom to top
    for i in range(start_index, -1, -1):
        heapify_max(combined, n, i)

    return combined