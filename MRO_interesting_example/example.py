from typing import Generic, TypeVar, Type

T = TypeVar('T')
D = TypeVar('D')

class BaseRepository(Generic[T]):
# class BaseRepository:
    def __init__(self, model: Type[T]):
        self.model = model
        print(f"BaseRepository initialized with model: {model}")

class DocumentRepository(BaseRepository[T], Generic[T, D]):
    def __init__(self, model: Type[T], document_model: Type[D]):
        super().__init__(model)
        self.document_model = document_model
        print(DocumentRepository.mro())
        print(f"DocumentRepository initialized with document_model: {document_model}")

DocumentRepository(int, str)


class DocumentRepository(Generic[T, D], BaseRepository[T]):
    def __init__(self, model: Type[T], document_model: Type[D]):
        super().__init__(model)
        self.document_model = document_model
        print(DocumentRepository.mro())
        print(f"DocumentRepository initialized with document_model: {document_model}")
        

print("="*100)
DocumentRepository(int, str)
# SAME BEHAVIOR




# Custom classes:

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self):
        print(C.mro())

print("="*100)
print("CUSTOM CLASSES")
C()

class C(B, A):
    def __init__(self):
        print(C.mro())
   

print("="*100)
C()


# ANOTHER TESTS




class DocumentRepository(A, BaseRepository[T]):
    def __init__(self):
        print(DocumentRepository.mro())
        

print("="*100)
DocumentRepository()


class DocumentRepository(BaseRepository[T], A):
    def __init__(self):
        print(DocumentRepository.mro())
        

print("="*100)
DocumentRepository()