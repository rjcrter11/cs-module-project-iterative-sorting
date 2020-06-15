# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Set first element as minimum
        # check if element < minimum
        # if it is, set element as new minimum
        # at the end of the list, the smallest found element is switched with
        # the element that the loop started on

        cur_index = i
        smallest_index = cur_index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


def selection_sort_alt(arr):
    curr_index = 0
    while curr_index < len(arr):
        smallest = min(arr[curr_index:])
        smallest_index = arr.index(smallest)
        arr[curr_index], arr[smallest_index] = arr[smallest_index], arr[curr_index]
        curr_index += 1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Compare left element and right element
    # if left element > right element, swap them
    # Repeat til sorted
    i = 0
    while i < len(arr) - 1:
        j = 0
        while j < len(arr) - 1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
            j += 1
        i += 1

    return arr


def bubble_sort_alt(arr):
    for i in range(0, len(arr)):
        swapped = False
        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            i = i + 1
        if swapped == False:
            break
    return arr


def bubble_sort_alt_2(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [12, 18, 6, 3, 7, 19, 11, 4, 5, 13, 17]
print(arr)
# print(selection_sort(arr))
# print(bubble_sort(arr))
# print(bubble_sort_alt(arr))
# print(bubble_sort_alt_2(arr))
print(selection_sort(arr))

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):

    return arr
