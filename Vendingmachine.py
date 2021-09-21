class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))

if __name__ == "__main__":
    carton_of_bottles = VendingMachine()

    print("How many bottles were sold?")
    amount = int(input())
    carton_of_bottles.purchase(amount)

    print("How many bottles were restocked?")
    amount = int(input())
    carton_of_bottles.restock(amount)

    carton_of_bottles.get_inventory

    carton_of_bottles.report()
