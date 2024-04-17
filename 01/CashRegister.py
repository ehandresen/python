class CashRegister:
    # class has to properties: item_count & total_price
    def __init__(self):
        self.item_count = 0
        self.total_price = 0.0
    
    def add_item(self, price):
        self.item_count += 1
        self.total_price += price
    
    def get_count(self):
        return f'Items: {self.item_count}'
    
    def get_total(self):
        return f'Total: ${self.total_price}'