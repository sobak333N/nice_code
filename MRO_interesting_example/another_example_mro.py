from abc import ABC, abstractmethod

class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(ABC):
    pass

class E(B, D):
    pass

class Final(C, E):
    def __init__(self):
        print(Final.mro())


print(f"{C.mro()=}")
print(f"{E.mro()=}")


Final()

class Final(E, C):
    def __init__(self):
        print(Final.mro())
        
Final()
