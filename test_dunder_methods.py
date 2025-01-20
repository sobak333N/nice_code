class Test:
    counter_instance = 0
    def __new__(cls, *args, **kwargs):
        print("NEW!")
        cls.counter_instance+=1
        instance = super().__new__(cls)
        print("AFTER NEW")
        return instance

    def __init__(self, first, second):
        self.first = first
        print("SELF")
        self.second = second


test1 = Test(1,2)
print(dir(test1))