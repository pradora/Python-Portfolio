#ToniP
#INF103
#tipTaxTotal


#ask user to enter the charge for the food
bill = float(input('Enter total amount of bill:'))

#calculate the amount of 18% tip and 7% tip
tip1 = bill * .18
tip2 = bill * .07
total = tip1 + tip2 + bill       
#dispaly each amount and total
print('Bill:',bill)
print('18% tip:', format(tip1, '.2f'))
print('7% tax:', format(tip2, '.2f'))
print('Your total bill is:',format(total, '.2f'))
