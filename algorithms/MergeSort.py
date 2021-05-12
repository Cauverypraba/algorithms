def mergeSort(array):
    if len(array) > 1:
        print('print')
        r = len(array) // 2
        L = array[:r]
        R = array[r:]
        print('array',array)
        mergeSort(L)
        mergeSort(R)
        print(L, R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            print('//',L[i],R[i])
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            print(',,',L[i])
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            print(',,',R[j])
            array[k] = R[j]
            j += 1
            k += 1    
    print(';;',array)

array = [6, 5, 12, 10, 9, 1]
mergeSort(array)
