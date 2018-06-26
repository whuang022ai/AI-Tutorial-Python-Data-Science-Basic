import numpy as np

price = np.array([230, 330, 500, 220, 150, 600, 200])
people = np.array([100, 87, 90, 150, 250, 60, 120])


def print_price():
    room_id = input('Enter your room id :')
    print('The price of room is :', price[int(room_id)])
    return


def get_max_price():
    print('The max price is', price.max())
    print('The room that has max price is', price.argmax())
    return


def get_min_price():
    print("The min price is", price.min())
    print('The room that has min price is', price.argmin())
    return


def get_total_income():
    print('Total income is', np.dot(price, people))
    return


def get_max_income():
    income = price*people
    print('The max income is', income.max())
    print('The room that has max income is', income.argmax())
    return


def display_price_loop():
    print(price.size)
    for i in range(int(price.size)):
        p = price[i]
        print(p)
    return


display_price_loop()
