class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity > 0: 
            self.capacity = capacity
            self.myList = []
            self.myLength = 0

    def get(self, i: int) -> int:
        return self.myList[i]

    def set(self, i: int, n: int) -> None:
        self.myList[i] = n

    def pushback(self, n: int) -> None:

        if self.myLength >= self.capacity: 
            self.resize()

        self.myList.append(n)
        self.myLength += 1
         


    def popback(self) -> int:
        
        self.myLength -=1
        return self.myList[self.myLength]

    def resize(self) -> None:
        self.capacity *=2

    def getSize(self) -> int:
        return self.myLength
    
    def getCapacity(self) -> int:
        return self.capacity