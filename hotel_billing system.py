menu = {  'pizza': 90,
          'burgar':60,
          'sandwich':70,
          'samosa':40,
          'noodels':80
        }

print("Welcome to KARAN's restorant\n")
print('pizza: 90$\nburgar: 60$\nsandwich:70$\nsamosa: 40$\nnoodels :80$')
total_order = 0
qun = 1
order_1 = input('\nenter name of your order you want to order::')
qun = input('enter the quntity of your order: ')
print('\n')
if order_1 in menu:
    total_order += (menu[order_1]*int(qun))
    print("your order is succesfully added \n")
else:
    print('Given Order is not avalable in our menu.\n')
    print('please order somthing else ::')

for i in range(100):
    another_order = input("do you want any athor item(yes/no)\n")
    if another_order == 'yes':
        order_2 = input('enter name of another item you want to order ::')
        qun = input('enter the quntity of your order:')
        
        if order_2 in menu:
            total_order += menu[order_2]*int(qun)
            print("your order is succesfully added \n")  
        else:
                print('Given Order is not avalable in our menu.\n')
                print('please order somthing else ::')
    else:
        print("thank you for using our service")
        break


       
print(f'your Total amount of bill is: {total_order}$')
