# Created By Amin Zeina 
# Created on Mar 2018
# Calculates cost of a pizza depending on size and # of toppings

pizza_size = input( '''
What size would you like your pizza?

Type "large" for a Large Pizza.
Type "extra large" for an Extra Large Pizza.

''')

if pizza_size == 'large' or pizza_size == 'extra large':
	toppings = int(input( 'Enter how many toppings you would like between 1 and 4: '))
	if pizza_size == 'large':
		if toppings == 1:
			subtotal = 6 + 1 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 2:
			subtotal = 6 + 1.75 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 3:
			subtotal = 6 + 2.50 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total), 2)	)
		elif toppings == 4:
			subtotal = 6 + 3.35 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		else:
			print('Invalid # of toppings. Please restart and choose a value between 1 and 4.')
	elif pizza_size == 'extra large':
		if toppings == 1:
			subtotal = 10 + 1 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 2:
			subtotal = 10 + 1.75 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 3:
			subtotal = 10 + 2.50 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total), 2)	)
		elif toppings == 4:
			subtotal = 10 + 3.35 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		else:
			print('Invalid # of toppings. Please restart and choose a value between 1 and 4.')
	else:
	    print( 'Invalid size. Please restart and type "large" or "extra large" only.')
else: 
	print( 'Invalid size. Please restart and type "large" or "extra large" only.')


input('Program End.')