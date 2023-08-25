#ask user to enter the amount of a purchase
purchase = float(input('Please enter amount of purchase: '))
#compute state (.025)
state = purchase * .025
#and county sales tax (.05)
county = purchase * .05
#display purchase, state tax, count sales tax, total sale
print (purchase)
print (state)
print (county)
total = purchase + state + county
print (total)
