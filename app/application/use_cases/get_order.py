from app.application.interfaces.order_repository import IOrderRepository
from app.infra.repositories.order_repository import OrderRepository
from fastapi import HTTPException
from app.domain.schemas import OrderRead

class GetOrderUseCase:
    """
    Caso de uso para consultar una orden por ID.
    """
    def __init__(self, db_session):
        self.repository: IOrderRepository = OrderRepository(db_session)

    async def execute(self, order_id: str) -> OrderRead:
        order = await self.repository.get_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Orden no encontrada")
        return OrderRead(
            order_id=order.id,
            product_id=order.product_id,
            user_id=order.user_id,
            created_at=order.created_at.isoformat()
        )
