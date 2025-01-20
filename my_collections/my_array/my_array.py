from pydantic import BaseModel
from typing import List, Any, Optional


class MyList(BaseModel):
    my_list: List = []
    size: int = 2
    cur_size: int = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_list = [None]*self.size
    
    def __getitem__(self, index: int):
        return self.my_list[index]

    def __setitem__(self, index: int, item: Any):
        self.my_list[index] = item

    def __len__(self):
        return self.cur_size
     
    def append(self, item: Any):
        if self.cur_size == self.size:
            new_array = [None]*(int(self.size*1.5))
            for index, num in enumerate(self.my_list):
                new_array[index] = num
            self.my_list = new_array
            self.size = len(self.my_list)

        self.my_list[self.cur_size] = item
        self.cur_size += 1
    
    def remove(self, item: Any):
        self.cur_size -= 1
        for index, num in enumerate(self.my_list):
            if num == item:
                del self.my_list[index]
                return
        self.cur_size += 1
        raise ValueError("No such element")

    def pop(self, index: int=-1):
        self.cur_size -= 1
        if index == -1 and self.cur_size!=-1:
            self.my_list[self.cur_size] = None
            return
        for i, num in enumerate(self.my_list):
            if i == index:
                del self.my_list[index]
                return
        self.cur_size += 1
        raise IndexError("No such index")

    def __iter__(self):
        for i in range(self.cur_size):
            yield self.my_list[i]

