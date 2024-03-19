''' Insertion sort algorithm in python '''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

def get_user_input():
    numbers_string = input("Enter a list of numbers separated by spaces: ")
    arr = [int(num) for num in numbers_string.split()]
    return arr

arr = get_user_input()  
insertion_sort(arr)
print(arr)
