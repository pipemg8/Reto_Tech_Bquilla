from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id: str
    user_id: str

class OrderResponse(BaseModel):
    order_id: str

class OrderRead(BaseModel):
    order_id: str
    product_id: str
    user_id: str
    created_at: str
