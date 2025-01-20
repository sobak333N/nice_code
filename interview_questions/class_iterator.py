

class Nums:
    def __init__(self, n: int):
        self.n = n
        self.cur = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.cur % 3 ==0:
            self.cur+=1
        if self.cur >= self.n:
            raise StopIteration
        tmp = self.cur
        self.cur+=1
        return tmp
    

for i in Nums(10):
    print(i)