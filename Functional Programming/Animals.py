def describe_pet(animal_type, pet_name):
    """Display all information about the pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title + ".")
    
    describe_pet('great white', 'jaws')
    describe_pet('Tyranasuarus Rex', 'Tiny hands')
    
