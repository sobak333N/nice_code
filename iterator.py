
class Squares():
    def __init__(self, limit: int):
        self.limit = limit
        self.cur_val = 0 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_val >= self.limit:
            raise StopIteration
        self.cur_val+=1
        return (self.cur_val-1)**2


s = Squares(10)

for i in s:
    print(i)