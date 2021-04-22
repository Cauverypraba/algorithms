'''Bubble Sort Algorithm using Python.'''
def bubbleSort(array):    
    j = 0
    length = len(array)
    for i in range(0, length-1):
        # check array is in descending order
        if i < length-1 and array[i] < array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
            j += 1
    length = j
    array2 = array[:]
    print(array,array2)
    array2.sort(reverse = True)
    # check both array is in descending order else return to bubbleSort()
    if array == array2:
        print(array)
    else:
        bubbleSort(array)        
    
    # ckeck array is in ascending order
    # if array == sorted(array):
    #     print(array)
    # else:
    #     bubbleSort(array)    

array = [-2, 45, 0, 11, 10] 
bubbleSort(array) 

# def bubbleSort(array):
    
#   # loop through each element of array
#   for i in range(len(array)):
#     print(i)
#     # loop to compare array elements
#     for j in range(0, len(array) - i - 1):
#       print('jjj',j)
#       # compare two adjacent elements
#       # change > to < to sort in descending order
#       if array[j] > array[j + 1]:

#         # swapping occurs if 
#         # the first element is greater than second
#         temp = array[j]
#         array[j] = array[j+1]
#         array[j+1] = temp
#         print(array)  


# data = [-2, 45, 0, 11, -9]

# # call the bubbleSort() method
# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)          