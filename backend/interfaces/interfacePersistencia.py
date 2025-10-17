from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar("T")  # Tipo genérico para cualquier modelo

class IRepository(ABC, Generic[T]):
    @abstractmethod
    def save(self, entity: T):
        pass
