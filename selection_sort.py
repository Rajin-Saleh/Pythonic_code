

''' from small to big ang big to bigger to infinity. '''

''' Working with current minimum and it goes form left to right side '''



def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j 

        
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]   #swap

arr = [2, 6, 5, 1, 3, 4, 7]
selection_sort(arr)
print(arr)





