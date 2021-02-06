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
def file_writer(value):
    with open('matrix.csv', 'w') as file:
        csv_writer = csv.writer(file)
        for row in value:
            csv_writer.writerow(row)


# Matrix generator function, takes number or rows(n) and columns(m)
def matrix_generator(n, m, range_min = -5000, range_max = 5000):
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


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


#Modified bublesort function that works a lot faster than original
def bubblesort(nums):
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

@benchmark
def main():
    m_h = 1000
    m_w = 1000
    matrix = matrix_generator(m_h, m_w)
    matrix_flat = []

    for i in range(m_h):
        matrix_flat += matrix[i]

    matrix_quick = quickSort(matrix_flat,0, len(matrix_flat)-1)
    #matrix_buble = bubblesort(matrix_flat)

    matrix = []
    for i in range(0, m_h * m_w, m_w):
        matrix += [matrix_flat[i:i + m_w]]

    file_writer(matrix)


if __name__ == '__main__':
    main()

