from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Customer, Server, Manager


def main():
    # add pizza to the manu
    pizza_1 = Pizza('chiken pizza', 650, 'large', ['chiken', 'sugger', 'testing solt', 'masala', 'onion', 'oil'])
    pizza_2 = Pizza('beef pizza', 850, 'large', ['onion', 'oil', 'beef', 'sugger', 'testing solt', 'masala'])
    pizza_3 = Pizza('fish pizza', 550, 'large', ['fish', 'sugger', 'onion', 'oil', 'testing solt', 'masala'])

    menu = Menu('Food Menu')
    menu.add_menu_item('pizza', pizza_1)
    menu.add_menu_item('pizza', pizza_2)
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the manu
    burger_1 = Burger('Beef burger', 480, 'beef', ['none bread', 'chili sos', 'salat', 'egg', 'chis'])
    burger_2 = Burger('chiken burger', 380, 'chiken', ['none bread', 'chili sos', 'salat', 'egg', 'chis'])
    menu.add_menu_item('burger', burger_1)
    menu.add_menu_item('burger', burger_2)

    # add drinks to the manu
    drink_1 = Drinks('Coca cola', 120, True)
    drink_2 = Drinks('Pepsi', 110, True)
    coffe = Drinks('Mocha', 300, False)
    menu.add_menu_item('drinks', drink_1)
    menu.add_menu_item('drinks', drink_2)
    menu.add_menu_item('drinks', coffe)

    menu.show_manu()

    # create a restaurant here
    restaurant = Restaurant('Glora jean\'s', 2000, menu)
    
    # add employee
    manager = Manager('Habibor Rahaman', '0177837823', 'habibor12@gmail.com', 'mohammodpur', '1923891238', 40000, 'january 1 - 01 - 2022', 'core')
    restaurant.add_employee('manager', manager)
    chef = Chef('hanif', '017872378', 'hanif1@gmail.com', 'nowpara', '2093893204', 18000, '2 januery', 'cooking', ['rost', 'polau', 'pizza', 'tika'])
    restaurant.add_employee('chef', chef)

    server = Server('rifat', '013898342', 'rifat12@gmail.com', 'wari', '728373821', 23000, '1 march', 'food delivary')
    restaurant.add_employee(server)

if __name__ == '__main__':
    main()