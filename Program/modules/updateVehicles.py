def updateVehicles(vehicles, vehicle):
    '''
    A variable is defined dedicated to
    controlling the function if the car exists or not.
    '''
    i = False
    
    '''
    The rest of the function is executed and the car to 
    be modified is searched and depending on the user's option,
    only the year or the year and the brand or the car
    are modified completely.
    '''
    
    for vehicleF in vehicles: 
        if vehicleF["model"] == vehicle["model"] and vehicleF["year"] == vehicle["year"]:
            i = True
            option = input("que desea modificar? 1.-Marca 2.-Modelo 3.-año")
            
            if option == "1":
                vehicleF["brand"] = input("añada nueva marca")
                vehicleF["model"] = input("añada nueo modelo\n")
                vehicleF["year"] = input("indica nuevo año")
            elif option == "2":
                vehicleF["model"] = input("añada nueo modelo\n")
                vehicleF["year"] = input("introduzca el año")
            elif option == "3":
                vehicleF["year"] = input("añada nueo año\n")


    if i == False:
        print("no se encontro el coche")
        
    return vehicles
