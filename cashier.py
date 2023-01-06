item_name= input('Input menu: ')
price= int(input('Input Price of menu: '))
Quantity = int(input('input your Quantity:'))
Quantity2 = price * Quantity
total_Money = int(input('Input your money: '))
return_money = total_Money - Quantity2

teks = f'''
Name item: {item_name}
Price: {price}
Quantity: {Quantity}
Total Price: {Quantity2}
Total Money: {total_Money}
Return: {return_money}

'''

file = open('Nota.txt', 'w')

file.write(teks)

