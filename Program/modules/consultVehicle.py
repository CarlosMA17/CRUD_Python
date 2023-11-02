def consultVehicle(vehicle):
    if vehicle != {}:
        message = vehicle["brand"] + " " + vehicle["model"] + " (" + vehicle["year"] + ")"
    else: 
        message = "no existe el coche"
    print(message)