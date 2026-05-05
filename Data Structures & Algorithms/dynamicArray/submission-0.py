class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.size = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if(self.size == len(self.array)):
            self.resize()
        
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        lastElement = self.array[self.size - 1]
        self.size -= 1
        return lastElement
 

    def resize(self) -> None:
        newArray = [0] * (len(self.array) * 2)

        for i in range(self.size):
            newArray[i] = self.array[i]
        
        self.array = newArray
        self.capacity = len(self.array)



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
