availible_cars = ['Ford Mustang', 'Subaru WRX sti', 'Mitsubishi Evo',
                  'Nissan 240']
requested_cars = 'Subaru WRX sti', 'Ford Mustang'']
for requested_cars in requested_cars:
    if requested_car in availible_cars:
        print("Adding " + requested_car + ".")
    else:
      print("Sorry we dont have " + requested_car + ".")
      print("\nFinished making the right car purchase")
