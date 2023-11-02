def consultVehicle(vehicle):
    
    '''
    If the vehicle is not an empty dictionary,
    it shows the car in a line that is more readable for the user.
    '''
    
    if vehicle != {}:
        message = vehicle["brand"] + " " + vehicle["model"] + " (" + vehicle["year"] + ")"
    else: 
        message = "no existe el coche"
    print(message)