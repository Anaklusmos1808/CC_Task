class Role:
    def __init__(self, role, name='Test'):
        assert role == 'Admin' or role == 'Consumer', 'Please enter either Admin or Consumer as role'

        self.__role = role
        self.name = name

    @property
    def role(self):
        return self.__role


class Product:
    

    def __init__(self, name, cost, category, quantity, discount=False, profit_margin=0.1,discount_rate = 0.9 ):

       
        self.name = name
        self.category = category
        self.discount = discount
        self.quantity = quantity
        self.discount_rate = discount_rate
        

        if self.discount:
            self.actualCost = float(cost) * self.discount_rate
        if not self.discount:
            self.actualCost = float(cost)

        self.cost = (self.actualCost * profit_margin) + self.actualCost

       
class Inventory:
    dummyData = [Product('name1', 100, 'misc', 4, True, 0.1, 0.8), Product('name2', 100, 'fruit', 2),
                 Product('name3', 10, 'misc', 1), Product('name4', 5, 'misc', 10, True),
                 Product('name5', 5, 'fruit', 3, True)]  # just like with book and shelf

    def __init__(self):
        pass
       

    def total_cost(self, productList):
        self.inventoryValue = 0
        for product in productList:
            productValue = product.quantity * product.cost
            self.inventoryValue += productValue

        return self.inventoryValue

    def calculate_profit(self, user: Role, productList):
        self.profit = 0
        try:
            if user.role == 'Admin':
                for product in productList:
                    profitValue = (product.cost - product.actualCost)*product.quantity
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
                self.cart.append(Product(name, product.cost, category, quantity))
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
            print(round(profit)) #was getting a floating point error
            print(total_cost)
        else:
            print(total_cost)


user = Role('Admin')
inventory = Inventory()
cart = Cart()
cart.add_item('name1', 2, 'misc')

cart.generateBill(user=user)
