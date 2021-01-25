#This is code for selection sort
#It works by choosing the smallest value remaining in the list each time
#and adding it to the sorted part of the list until the entire list is sorted

def find_smallest_number(lst, start_index):
    minimum_index = start_index
    for i in range(start_index+1, len(lst)):
        if lst[i] < lst[minimum_index]:
            minimum_index = i
    return minimum_index

def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
    return lst

def selection_sort(lst):
    for list_sorted_until in range(0, len(lst)):
        next_number_index = find_smallest_number(lst, list_sorted_until)
        lst = swap(lst, list_sorted_until, next_number_index)
    return lst
