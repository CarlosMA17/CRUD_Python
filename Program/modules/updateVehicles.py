def updateVehicles(vehicles, vehicle):
    i = False
    for vehicleF in vehicles: 
        if vehicleF["model"] == vehicle["model"] and vehicleF["year"] == vehicle["year"]:
            option = input("que desea modificar? 1.-Marca 2.-Modelo 3.-año")
            if option == "1":
                vehicleF["brand"] = input("añada nueva marca")
                vehicleF["model"] = input("añada nueo modelo\n")
                vehicleF["year"] = input("indica nuevo año")
                i = True
            elif option == "2":
                vehicleF["model"] = input("añada nueo modelo\n")
                vehicleF["year"] = input("introduzca el año")
                i = True
            elif option == "3":
                vehicleF["year"] = input("añada nueo año\n")


    if i == False:
        print("no se encontro el coche")
    return vehicles
