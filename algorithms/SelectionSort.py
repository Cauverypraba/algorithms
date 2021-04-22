''' Implementation of Selection Sort '''
class SelectionSort():
    def __init__(self):
        self.j = 0
        self.c = 0
        
    def sort(self, array):
        min = array[0]
        for i in range(self.j, len(array)):
            for z in range(i, len(array)):
                if i < len(array)-1 and z < len(array)-1 and min > array[z+1]:
                    min = array[z+1]
                else:    
                    min = min
                    self.c = array.index(min)    
            array[self.j], array[self.c] = array[self.c], array[self.j]
            if i < len(array)-1:
               min = array[i+1]
            self.j += 1
            # print(array)    
        if array == sorted(array):
            print(array)
        else:
            self.sort(array)            

array = [20, 50, 2, 15, 22]
ss = SelectionSort()
ss.sort(array)

