class Order:
    def __init__(self, total):
        self.total = total

    def calculate_total(self):
        return self.total


class DineInOrder(Order):
    def calculate_total(self):
        return self.total * 1.12  


class TakeAwayOrder(Order):
    def calculate_total(self):
        return self.total * 0.9  


class DeliveryOrder(Order):
    def calculate_total(self):
        return self.total + 60  
    
for o in [DineInOrder(950), TakeAwayOrder(850), DeliveryOrder(1300)]:
    print(o.calculate_total())
