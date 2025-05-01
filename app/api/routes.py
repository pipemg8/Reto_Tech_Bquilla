from fastapi import APIRouter
from app.api.v1.endpoints import orders

router = APIRouter()
router.include_router(orders.router, prefix="/v1/orders", tags=["Orders"])
