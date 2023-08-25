#ToniP
#INF103
#Total Purchase

#ask for the price of each item
one = float(input('Enter the price of first item: '))
two = float(input('Enter the price of second item: '))
three = float(input('Enter the price of third item: '))
four = float(input('Enter the price of fourth item: '))
five = float(input('Enter the price of fifth item: '))
six = one+two+three+four+five
#displays the subtotal of the sale
print('Your subtotal is: ', format(six, '.2f'))
#displays the amount of sales tax(.07)
salestax = float(six) * .07
print('Your sales tax is: ', format(salestax, '.2f'))
# the total of sales and sales tax
total = float(six) + float(salestax)
print('Your total with tax is: ', total)

