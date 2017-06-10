def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' '  + last_name
    return full_name.title()

# This is an Infinite loop !
while True:
    print("\nPlease tell me your:")
    print("(enter 'q' at any time to quit)")
    f_name = input("Firstname: ")
    if f_name == 'q':
        break
    l_name = input("Lastname: ")
    if l_name = 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
