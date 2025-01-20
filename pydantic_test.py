from typing import Any
from pydantic import BaseModel, model_validator
from datetime import date

class Event(BaseModel):
    name: str
    start_date: date
    end_date: date

    # Валидатор, работающий в режиме `pre` (получаем словарь входных данных)
    @model_validator(mode='before')
    @classmethod
    def preprocess(cls, values) -> dict[str,Any]:
        print(type(values))
        # Здесь values — это словарь, и можно, например, изменить формат или произвести предварительную проверку
        print("Pre validator, values:", values)
        return values

    # Валидатор, работающий в режиме `after` (получаем уже созданный объект модели)
    @model_validator(mode='after')
    def check_dates(cls, model_obj):
        print(type(model_obj))
        # Здесь model_obj — это экземпляр модели Event
        # if model_obj.start_date > model_obj.end_date:
        #     raise ValueError("start_date must be earlier than end_date")
        return model_obj

# Пример использования:
try:
    event = Event(name="Conference", start_date="2025-01-10", end_date="2025-01-05")
    print(type(event))
except ValueError as e:
    print("Validation error:", e)
