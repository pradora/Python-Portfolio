#ToniP
#INF103
#celsiusToFahrenheitTempatureConverter

#converts celsius to fahrenheit
#formula: F=9/5C + 32
#user enter tempature in Celsius
temp = int(input('Enter tempature in Celsius:'))



#display tempature in Fahrenheit
Fah = (9/5 * temp) + 32

if Fah >= 90:
    print('It\'s very hot outside')
if Fah <= 30:
    print('It\'s very cold outside')
if Fah < 90 and Fah > 30:
    print('It\'s Nice outside')
    
print('The tempature in Fahrenheit is:', Fah)

