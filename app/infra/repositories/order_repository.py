from app.application.interfaces.order_repository import IOrderRepository
from app.domain.entities.order import Order
from app.infra.models import OrderModel

class OrderRepository(IOrderRepository):
    def __init__(self, db_session):
        self.db_session = db_session

    async def save(self, order: Order):
        db_order = OrderModel(
            id=order.id,
            product_id=order.product_id,
            user_id=order.user_id,
            created_at=order.created_at,
        )
        self.db_session.add(db_order)
        await self.db_session.commit()
        await self.db_session.refresh(db_order)

    async def get_by_id(self, order_id: str):
        return await self.db_session.get(OrderModel, order_id)
