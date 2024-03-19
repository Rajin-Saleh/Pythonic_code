'''
breakdown bigger problem into sub problem until they become simple to solve

choose pivot element( either last or random element )
store element less than pivot in left sub array
store element greater than pivot in right dub array
call quicksort recursively on left sub array
call quicksort recursively on right sub array

random example: 

[22, 11, 88, 66, 55, 77, 33, 44]
22 is i
33 is j 
44 is pivot

End result
[11, 22, 33, 44, 55, 66, 77, 88]


'''


def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos -1)
        quick_sort(arr, partition_pos + 1, right)



def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arr = [22, 11, 88, 55, 77, 66 , 33, 44]
quick_sort(arr, 0 ,len(arr) - 1)
print(arr)




