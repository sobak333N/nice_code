from typing import List, Optional, Any

def multiplication_list(nums: List[Any]) -> Optional[int]:
    if not nums:
        return None
    ans = 1
    for num in nums:
        if not isinstance(num, int):
            return None
        ans*=num
    return ans



def test_multiplication_list():
    # Тесты на корректные списки
    assert multiplication_list([1, 2, 3, 4]) == 24, "Ошибка при обычном списке"
    assert multiplication_list([0, 5, 10]) == 0, "Ошибка при списке с нулём"
    assert multiplication_list([7]) == 7, "Ошибка при списке с одним элементом"
    assert multiplication_list([-1, 2, 3]) == -6, "Ошибка при списке с отрицательными числами"
    
    # Тесты на пустой список
    assert multiplication_list([]) is None, "Ошибка при пустом списке"
    
    # Тесты на невалидные элементы
    assert multiplication_list([1, 2, "3"]) is None, "Ошибка при нечисловом элементе"
    assert multiplication_list([1, 2, None]) is None, "Ошибка при None в списке"
    assert multiplication_list([1, 2, 3.5]) is None, "Ошибка при вещественном числе"
    
    # Тесты на пограничные случаи
    assert multiplication_list([1]) == 1, "Ошибка при одном числе"
    assert multiplication_list([1, -1]) == -1, "Ошибка при смешанных числах"
    assert multiplication_list([1] * 1000) == 1, "Ошибка при большом списке"
    
    print("Все тесты пройдены успешно!")

# Запуск тестов
test_multiplication_list()
