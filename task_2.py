class Product:
    def __init__(self, name, price):
        self.name = name
        self.amount = 0
        self.price = price

    def increase_amount(self):
        self.amount += 1

    def decrease_amount(self):
        if self.amount > 0:
            self.amount -= 1
        else:
            print(f'товара {self.name} нет')

    def get_amount(self):
        print(self.amount)

    def get_cost(self):
        # print(self.amount, '*', self.price, self.amount * self.price)
        return self.amount * self.price


class WareHouse:
    def __init__(self):
        self.products = []
        self.selled_products = []

    def find_product(self, product):
        for i in range(len(self.products)):
            if self.products[i].name == product.name: 
                return True
            
        return False

    def add_product(self, product):
        if not self.find_product(product):
            self.products.append(product)
        product.increase_amount()

    def delete_product(self, product):
        for i in range(len(self.products)):
            if self.products[i].name == product.name:
                product = self.products.pop(i) 
                return 
            
        print(f'товара {product.name} нет на складе')
            
    def get_cost(self):
        return sum([product.get_cost() for product in self.products])


class Seller:
    def __init__(self, name):
        self.name = name
        self.sellings = []
        self.money = 0

    def sell_product(self, product, warehouse):
        if warehouse.find_product(product):
            warehouse.delete_product(product)
            product.decrease_amount()
            self.sellings.append((product.name, product.price, product.amount))

        else:
            print('продукт закончился')

    def get_report(self):
        for sell in self.sellings:
            print(sell[0], sell[1], sep=' : ')


apple = Product(name='яблоко', price=10)
potato = Product(name='картошка', price=15)

warehouse = WareHouse()
warehouse.add_product(apple)
warehouse.add_product(apple)
warehouse.add_product(apple)
warehouse.add_product(potato)
warehouse.add_product(potato)

apple.get_amount()
potato.get_amount()

print(warehouse.get_cost())

seller_1 = Seller(name='джон')
seller_1.sell_product(apple, warehouse)
seller_1.get_report()


# в файл выводится отчет о продажах
with open('report.txt', 'w') as file:
    for note in seller_1.sellings:
        print(f'Продано {note[0]}, по цене {note[1]}, оставшееся количество: {note[2]} ', file=file)
