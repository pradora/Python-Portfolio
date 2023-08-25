#ToniP
#INF103
#ingredientAdjuster

#for one cookie
#1.5 cups of sugar
SUGAR = 1.5/ 48

#1 cup of butter
BUTTER = 1/48

#2.75 cups of flour
FLOUR = 2.75 / 48

#recipe produce 48 cookies

#ask the user how many cookies they want to make
cookies = int(input('How many cookies to make:'))

#display how many cups each ingredient needs for the number of cookies
print(round(cookies * SUGAR),'Cups of Sugar')
print(round(cookies * BUTTER),'Cups of Butter')
print(round(cookies * FLOUR),'Cups of Flour')


