print('Welcome to coffee cafe')

def Welcome():
    print('Choose Your Order')
    print('Code----Coffee name---------price----')
    print('------------------------S-----M-----L')
    print('-A-------Espresso-------40----45---50')
    print('-B------Cappuccino------45----50---55')
    print('-C---------Mocha--------40----50---60')
    print('-D-----Black Coffee-----50----55---60')
    Order(0)

def Order(total_price):
    print('Enter coffee code Enter X To quite ==>', end=' ')
    Order_code = str(input())
    if Order_code not in 'ABCDX': return error(total_price)
    if Order_code == 'X': return showBill(total_price)
    Coffee_lst = {'A':'Espresso', 'B':'Cappuccino', 'C':'Mocha', 'D':'Black Coffee'}
    coffee_price = {'A':{'S':40, 'M':45, 'L':50},
                    'B':{'S':45, 'M':50, 'L':55},
                    'C':{'S':40, 'M':50, 'L':60},
                    'D':{'S':50, 'M':55, 'L':60}}
    order = Coffee_lst[Order_code]
    size = str(input('Choose Size (S/M/L)               ==> '))
    quantity = int(input('Enter Quantity                    ==> '))
    price = coffee_price[Order_code][size]
    total_order_price = price * quantity
    print(f'Name      {order}        {price}x{quantity}   =   {total_order_price}  baht.\n')
    return Order(total_order_price+total_price)

def error(x):
    print('------Invalid Coffee Code-------')
    return Order(x)

def showBill(bill):
    print('\n-------------------------------')
    print(f'Total          {bill}       baht')

Welcome()