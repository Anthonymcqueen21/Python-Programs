availible_toppings = ['mushrooms', 'olives', 'pepperoni', 
                      'tomatoes', 'onions', 'extra cheese']

requested_toppings = ['mushrooms', 'tomatoes', 'extra cheese']


for requested_topping in requested_toppings:
    if requested_topping in availible_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we dont have " + requested_topping + ".")
      
print("\nFinished making your pizza")



availible_cars = ['Ford Mustang', 'Subaru WRX sti', 'Mitsubishi Evo',
                  'Nissan 240']

requested_cars = 'Subaru WRX sti', 'Ford Mustang'']

for requested_cars in requested_cars:
    if requested_car in availible_cars:
        print("Adding " + requested_car + ".")
    else:
        print("Sorry we dont have " + requested_car + ".")
        
print("\nFinished making the right car purchase")
