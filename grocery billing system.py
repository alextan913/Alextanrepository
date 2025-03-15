print('=======================================')
print(' Welcome To Grocery Billing System')
print('=======================================\n')

total_cost = 0

while True:
    item_name = input("Enter the name of item (or type 'done' to finish): ")
    
    if item_name.lower() == 'done':
        break

    try:
        quantity = int(input(f'Enter the quantity of {item_name}: '))
        price_per_unit = float(input(f'Enter the price per unit of {item_name} (RM): '))

        if quantity < 0 or price_per_unit < 0:
            print('❌ Quantity and price must be positive numbers.\n')
            continue

        total_item_cost = quantity * price_per_unit
        print(f'✅ The total item cost for {item_name} is RM {total_item_cost:,.2f}.\n')
        total_cost += total_item_cost

    except ValueError:
        print('⚠️ Invalid input. Please enter numbers only for quantity and price.\n')
        continue

print('\n=======================================')
print(f'Total Cost: RM {total_cost:,.2f}')
print('=======================================')
print('🛒 Thank you for shopping with us! Have a great day!\n')

