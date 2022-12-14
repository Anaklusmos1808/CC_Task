class Role:
    def __init__(self, role, name='Test'):
        assert role == 'Admin' or role == 'Consumer', 'Please enter either Admin or Consumer as role'

        self.__role = role
        self.name = name

    @property
    def role(self):
        return self.__role


class Product:

    def __init__(self, name, cost, category, quantity, discount=False, profit_margin=0.1, discount_rate = 0.9):


        self.name = name
        self.category = category
        self.discount = discount
        self.quantity = quantity
        self.profit_margin = profit_margin
        self.discount_rate = discount_rate

        self.actualCost = float(cost)
        self.cost = (self.actualCost * self.profit_margin) + self.actualCost

        if self.discount:
            self.sellingCost = self.cost * self.discount_rate
        if not self.discount:
            self.sellingCost = self.cost

       

class Inventory:
    #can add discount rate and profit margin for product individually, the default is 0.9 and 0.1, also set disount = True or false
    dummyData = [Product('name1', 100, 'misc', 4, True, 0.2 ,0.9), Product('name2', 100, 'fruit', 2),
                 Product('name3', 10, 'misc', 1), Product('name4', 5, 'misc', 10, True),
                 Product('name5', 5, 'fruit', 3, True,0.5, 0.8)] 

    def __init__(self):
        pass
       
    def total_cost(self, productList):
        self.inventoryValue = 0
        for product in productList:
            productValue = product.quantity * product.sellingCost
            self.inventoryValue += productValue

        return self.inventoryValue

    def calculate_profit(self, user: Role, productList):
        self.profit = 0
        try:
            if user.role == 'Admin':
                for product in productList:
                    profitValue = (product.sellingCost - product.actualCost) * product.quantity
                    self.profit += profitValue

                return self.profit

            else:
                print("You don't have access to this function")

        except AttributeError:
            print('Please enter a valid username or list of products')


class Cart(Inventory):

    def __init__(self):
        self.cart = []
        super().__init__() 

    def add_item(self, name, quantity, category):
        for product in self.dummyData:
            if product.name == name and product.category == category and product.quantity >= quantity:
                addProduct = Product(name=name, cost=product.actualCost, category=category, quantity=quantity,
                                     discount=product.discount, profit_margin=product.profit_margin,
                                      discount_rate=product.discount_rate)
                self.cart.append(addProduct)
                print('product added to cart!')
                return

            else:
                print('product not in stock')

    def remove_item(self, item_del):
        try:
            for i in self.cart:
                if i.name == item_del:
                    self.cart.remove(i)
            print('Item has been removed')

        except AttributeError:
            print('Please try with a valid username')

    @staticmethod
    def generateBill(user: Role):
        total_cost = (cart.total_cost(cart.cart))
        profit = cart.calculate_profit(user, cart.cart)

        if user.role == 'Admin':
            print('=======BILL======= \n')
            print(f'profit: {profit}')
            print(f'total_cost: {total_cost}')
        else:
            print('=======BILL======= \n')
            print(f'total_cost: {total_cost}')


user = Role('Admin')
cons = Role('Consumer')
inventory = Inventory()
cart = Cart()

cart.add_item('name1', 2, 'misc')
cart.generateBill(user)
