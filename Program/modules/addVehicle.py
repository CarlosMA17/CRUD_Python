def addVehicle(vehicles):
    
    '''
    The user is asked for the model year and brand
    to be added and it is added to the list and returned.
    '''
    
    brand = input("añada la marca\n")
    model = input("añada el modelo\n")
    year = input("añada el año de fabricacion\n")
    
    vehicle = {
        "brand": brand,
        "model": model,
        "year": year
    }
    vehicles.append(vehicle)
    return vehicles