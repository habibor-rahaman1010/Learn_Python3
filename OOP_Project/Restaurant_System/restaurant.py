
class Restaurant:
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name
        self.orders = []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        if (employee_type == 'chef'):
            self.chef = employee

        if(employee_type == 'server'):
            self.server = employee

        if(employee_type == 'manager'):
            self.manager = employee

    def add_order(self, order):
        self.orders.append(order)


    def receive_payment(self, order, amount, customer):
        if(amount >= order.bill):
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print(f'Not enough mony! pay more')
        
    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense: {amount} for {description}')
        else:
            print(f'Not enough mony to pay {amount}')

    def pay_salary(self, employee):
        print(f'Payinf salary for {employee.name} salary: {employee.salary}')
        if (employee.salary < self.balance):
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()

    def show_employee(self):
        print('\n-------------------Showing Employees----------------\n')
        if(self.manager is not None):
            print(f'name: {self.manager.name} with salary: {self.manager.salary}')

        if(self.chef is not None):
            print(f'name: {self.chef.name} with salary: {self.chef.salary}')

        if(self.server is not None):
            print(f'name: {self.server.name} with salary: {self.server.salary}')
