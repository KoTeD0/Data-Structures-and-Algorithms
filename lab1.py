import time
import csv
import random


# A wrapper function that shows us the execution time of the function
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {end - start}')
        return return_value

    return wrapper


# File writer function, rewrites file.
def fileWriter(value):
    with open('matrix.csv', 'w') as file:
        csv_writer = csv.writer(file)
        for row in value:
            csv_writer.writerow(row)


# Matrix generator function, takes number or rows(n) and columns(m)
def matrixGenerator(n, m, range_min=-5000, range_max=5000):
    return [[random.randint(range_min, range_max) for row in range(n)] for column in range(m)]


# Function to partition the array on the basis of pivot element
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


# main quicksort func that calls help func partition, takes array, + pos 0 as low, and len of array - 1 as high
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Modified bublesort function that works a lot faster than original
def bubbleSort(nums):
    gap = len(nums)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(nums) - gap):
            j = i + gap
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                swaps = True
    return nums


# Comb Sort
def exchangeSort(data):
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True

# Default ShellSort func that takes array, and len -1
def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)

@benchmark
def main():
    m_h = 1000
    m_w = 1000
    matrix = matrixGenerator(m_h, m_w)
    matrix_flat = []

    for i in range(m_h):
        matrix_flat += matrix[i]

    # uncomment to make sort.
    # matrix_sorted = sorted(matrix)
    # matrix_quick = quickSort(matrix_flat,0, len(matrix_flat)-1)
    # matrix_bubble = bubbleSort(matrix_flat)
    # matrix_exchange = exchangeSort(matrix_flat)
    # matrix_shell = shellSort(matrix_flat, len(matrix_flat) - 1)
    # matrix_heap = heapSort(matrix_flat)

    matrix = []
    for i in range(0, m_h * m_w, m_w):
        matrix += [matrix_flat[i:i + m_w]]

    fileWriter(matrix)


if __name__ == '__main__':
    main()
# TODO: describe every sort func in docstring, how it works.
