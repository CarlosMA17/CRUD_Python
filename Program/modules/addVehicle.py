def addVehicle(vehicles):
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