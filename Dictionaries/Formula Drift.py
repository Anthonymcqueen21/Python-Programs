responses = []

#Set a barrier to indicate the Formula Drift series is relevant
polling_active = True

while polling_active:
    #Prompting the series name and the fans response.
    name = input("\nWhat is your favorite driver ?. ")
    response = input("Which driver other than the big sponsored will win serives ?")
    
    # Storing these responses withing dictionary .
    responses[name] = response 
    
    # Find out what the fans are saying about the future of the sport ?
    repeat = input("Do you see formula drift relevant ? (yes / no) ")
    if repeat = 'no':
        polling_active = False
        
# Polling is offically complete.
print("\n -- Final Results ---")
for name, response in responses.items():
    print(name + " would like to win the world championship " + response + ".")
    
