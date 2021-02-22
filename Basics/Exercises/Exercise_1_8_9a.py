mealPrice = eval(input('Enter Meal Price : '))
tipPercent = eval(input('Enter Tip Percent : '))

tipAmount = (tipPercent/100)*mealPrice
totalPrice = mealPrice + tipAmount
print('Final Price =',totalPrice,'Tip Amount =',tipAmount)