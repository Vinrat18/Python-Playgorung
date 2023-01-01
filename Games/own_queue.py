from typing import Generic, TypeVar


T = TypeVar("T", float, int)

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.__items = []
    
    def __str__(self) -> str:
        for item in self.__items:
            print(item)
        
        return ""
    
    def is_empty(self) -> bool:
       return not self.__items
    
    def enqueue(self, item: T) -> None:
       self.__items.append(item)
    
    def dequeue(self) -> T:
       return self.__items.pop(0) if self.is_empty() else None

    def size(self) -> int:
        return len(self.__items)

    def peek(self) -> T:
        return self.__items[0] if self.is_empty() else None

if __name__ == '__main__':
   q = Queue[int]()
   print(q.is_empty())
   q.enqueue(1)
   q.enqueue(2)
   print(q)
   print(q.dequeue())
   print(q)
   print(q.size())
   print(q.peek())    
