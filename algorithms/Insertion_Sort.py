'''Implementing Insertion Sort algorithm using Linked List'''
def insertionSort():
    for i in range(0, len(array)):
        if i < len(array)-1:
            # print(i)
            key = array[i+1]
            for j in range(0, i+1):
                if array[j] > key:
                    temp = array[j]
                    array[j] = array[i+1]
                    array[i+1] = temp
    print(array)                

array = [1, 0, 7, 2, 3]
insertionSort()                    