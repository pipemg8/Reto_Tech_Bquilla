from abc import ABC, abstractmethod
from app.domain.entities.order import Order

class IOrderRepository(ABC):
    @abstractmethod
    async def save(self, order: Order): pass

    @abstractmethod
    async def get_by_id(self, order_id: str): pass
