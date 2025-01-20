                    //     tail
//  NULL <- a <-> b <-> d <->c -> NULL

//                           tail        NULL<-NewNode->NULL
//  NULL <- a <-> b <-> d <->c -> NewNode

//                           tail        c<-NewNode->NULL
//  NULL <- a <-> b <-> d <->c <-> NewNode -> NULL



//         tail, head
//     NULL <- NewNode -> NULL

#include <iostream>

template <typename T>
class DLList {
private:
    // Внутренний класс для представления узлов списка
    struct Node {
        T data;
        Node* next;
        Node* prev;
        
        Node(T val) : data(val), next(nullptr), prev(nullptr) {}
    };
    
    Node* head;  // Указатель на первый элемент списка
    Node* tail;  // Указатель на последний элемент списка
    size_t size; // Размер списка
    
public:
    DLList() : head(nullptr), tail(nullptr), size(0) {}
    
    ~DLList() {
        clear();
    }
    
    // Метод для добавления элемента в конец списка
    void append(const T& value) {
        Node* newNode = new Node(value);
        
        if (tail) {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        } else {
            head = tail = newNode;
        }
        
        ++size;
    }
    
    // Метод для добавления элемента в начало списка
    void prepend(const T& value) {
        Node* newNode = new Node(value);
        
        if (head) {
            head->prev = newNode;
            newNode->next = head;
            head = newNode;
        } else {
            head = tail = newNode;
        }
        
        ++size;
    }
    




                     //     tail
//  NULL <- a <-> b <-> d <->c -> NULL

//                           tail        NULL<-NewNode->NULL
//  NULL <- a <-> b <-> d <->c -> NewNode

//                           tail        c<-NewNode->NULL
//  NULL <- a <-> b <-> d <->c <-> NewNode -> NULL



//         tail, head
//     NULL <- NewNode -> NULL





//        head                       tail
//  NULL <- a <-> b <-> d <->c <-> NewNode -> NULL



//        temp   head               tail
//  NULL <- a <-> b <-> d <->c <-> NewNode -> NULL


//        head               tail
//  NULL <- b <-> d <->c <-> NewNode -> NULL
// temp: a




    void removeFirst() {
        if (head) {
            Node* temp = head;
            head = head->next;
            
            if (head) {
                head->prev = nullptr;
            } else {
                tail = nullptr; // Список стал пустым
            }
            
            delete temp;
            --size;
        }
    }
    
    // Метод для удаления последнего элемента
    void removeLast() {
        if (tail) {
            Node* temp = tail;
            tail = tail->prev;
            
            if (tail) {
                tail->next = nullptr;
            } else {
                head = nullptr; // Список стал пустым
            }
            
            delete temp;
            --size;
        }
    }
    
    // Метод для получения элемента по индексу
//                    current 
//        head                       tail
//  NULL <- a <-> b <-> d <->c <-> NewNode -> NULL

// a = at(2)

    T& at(size_t index) {
        if (index >= size) {
            throw std::out_of_range("Index out of range");
        }
        
        Node* current = head;
        for (size_t i = 0; i < index; ++i) {
            current = current->next;
        }
        
        return current->data;
    }
    
    // Метод для очистки списка
    void clear() {
        while (head) {
            removeFirst();
        }
    }
    
    // Метод для получения размера списка
    size_t getSize() const {
        return size;
    }
    
    // Метод для вывода списка
    void print() const {
        Node* current = head;
        while (current) {
            std::cout << current->data << " <-> ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }
};

int main() {
    DLList<int> list;
    
    list.append(10);
    list.append(20);
    list.append(30);
    list.prepend(5);
    list.prepend(2);
    
    list.print(); // Ожидаемый вывод: 2 <-> 5 <-> 10 <-> 20 <-> 30 <-> nullptr
    
    std::cout << "Element at index 2: " << list.at(2) << std::endl; // Ожидаемый вывод: 10
    
    list.removeFirst();
    list.removeLast();
    
    list.print(); // Ожидаемый вывод: 5 <-> 10 <-> 20 <-> nullptr
    
    std::cout << "Size of the list: " << list.getSize() << std::endl; // Ожидаемый вывод: 3
    
    list.clear();
    
    std::cout << "Size after clearing: " << list.getSize() << std::endl; // Ожидаемый вывод: 0
    
    return 0;
}
