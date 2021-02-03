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
def matrix_generator(n, m):
    return [[random.randint(-5000, 5000) for row in range(n)] for column in range(m)]


# Quicksort function that made from WIKI pseudocode, using Hoar's algorithm.
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       pivot = nums[len(nums) // 2]
       less = []
       more = []
       pivotlist = []
       for n in nums:
           if n < pivot:
               less.append(n)
           elif n > pivot:
               more.append(n)
           else:
               pivotlist.append(n)
       return quicksort(less) + pivotlist + quicksort(more)
   

# Modified bublesort function that works a bit faster than original
def bublesort(nums):
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
def bublesort_checker():
    file_writer(bublesort(matrix_generator(1000,1000)))

@benchmark
def quicksort_checker():
    print((matrix_generator(1000, 1000)).sort())

quicksort_checker()