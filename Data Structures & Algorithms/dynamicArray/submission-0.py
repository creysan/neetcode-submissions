class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.dynamicArray = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.dynamicArray[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.dynamicArray[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        newDynamicArray = [0] * self.capacity

        for i in range(self.length):
            newDynamicArray[i] = self.dynamicArray[i]
        self.dynamicArray = newDynamicArray


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
