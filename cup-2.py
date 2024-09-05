class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.quantity + milliliters <= self.size:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity
cup = Cup(10, 5) 
print(cup.status()) 
cup.fill(4) 
cup.fill(2) 
print(cup.status())