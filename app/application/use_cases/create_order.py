from app.domain.entities.order import Order
from app.application.interfaces.order_repository import IOrderRepository
from app.infra.repositories.order_repository import OrderRepository
from app.utils.queue import InMemoryQueue
from app.utils.inventory import InventoryService
import logging

logger = logging.getLogger(__name__)

class CreateOrderUseCase:
    """
    Caso de uso para crear una orden.
    """
    def __init__(self, db_session):
        self.repository: IOrderRepository = OrderRepository(db_session)
        self.queue = InMemoryQueue()
        self.inventory = InventoryService()

    async def execute(self, order_data):
        if not self.inventory.is_available(order_data.product_id):
            logger.warning("Producto no disponible")
            raise ValueError("Producto no disponible")
        order = Order(**order_data.model_dump())
        await self.repository.save(order)
        self.queue.emit({"order_id": order.id})
        logger.info(f"Order created: {order.id}")
        return order
