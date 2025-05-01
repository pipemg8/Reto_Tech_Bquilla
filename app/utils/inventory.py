class InventoryService:
    """
    Servicio simulado para validar productos disponibles.
    """
    def __init__(self):
        self.available_products = {"prod-001", "prod-002", "chocolatina", "Galletas"}

    def is_available(self, product_id: str) -> bool:
        return product_id in self.available_products
