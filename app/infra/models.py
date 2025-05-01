from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC
import uuid

Base = declarative_base()

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
