print('Welcome To Grocery Billing System')

total_cost=0

while True:
    item_name=input("Enter the name of item (or type 'done' to finish):")
    if item_name=='done':
        break
    else:
        (item_name)
    try:
        quantity=int(input(f'Enter the quantity of {item_name}:'))
        price_per_unit=float(input(f'Enter the price per unit of {item_name}:'))
        if quantity<0 or price_per_unit<0:
            print('Both of them must be in positive number.')
            continue
    except ValueError:
        print('Invalid value.Please enter the quantity and price.')
        continue
    total_item_cost=quantity*price_per_unit
    print(f'The total item cost of {item_name} is RM {total_item_cost:,.2f}.')

    total_cost+=total_item_cost
print(f'Total Cost=RM{total_cost:,.2f}')
print('Thank you for shopping with us')
