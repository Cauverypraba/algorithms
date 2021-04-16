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
                    # print('if',min)
                else:    
                    min = min
                    # print('else',min)
                    self.c = array.index(min)
        # print(array[j], array[c])
            # print(self.j, self.c, min)    
            array[self.j], array[self.c] = array[self.c], array[self.j]
            if i < len(array)-1:
               min = array[i+1]
            self.j += 1
            # print(array)    
        if array == sorted(array):
            print(array)
        else:
            # min = array[i+1]
            self.sort(array)            

array = [20, 50, 2, 15, 22]
ss = SelectionSort()
ss.sort(array)