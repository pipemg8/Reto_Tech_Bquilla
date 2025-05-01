import uuid
from datetime import datetime, UTC

class Order:
    """
    Entidad del dominio que representa una orden.
    """
    def __init__(self, product_id: str, user_id: str):
        self.id = str(uuid.uuid4())
        self.product_id = product_id
        self.user_id = user_id
        self.created_at = datetime.now(UTC)
