from fastapi import APIRouter, Depends, status
from app.domain.schemas import OrderCreate, OrderResponse, OrderRead
from app.application.use_cases.create_order import CreateOrderUseCase
from app.application.use_cases.get_order import GetOrderUseCase
from app.infra.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    """
    Endpoint para crear una nueva orden.
    """
    use_case = CreateOrderUseCase(db)
    result = await use_case.execute(order)
    return OrderResponse(order_id=result.id)

@router.get("/{order_id}", response_model=OrderRead)
async def get_order(order_id: str, db: AsyncSession = Depends(get_db)):
    """
    Endpoint para consultar una orden existente.
    """
    use_case = GetOrderUseCase(db)
    return await use_case.execute(order_id)
