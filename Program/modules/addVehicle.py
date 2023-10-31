def addVehicle(vehicles):
    brand = input("añada la marca")
    model = input("añada el modelo")
    year = input("añada el año de fabricacion")
    
    vehicle = {
        "brand": brand,
        "model": model,
        "year": year
    }
    vehicles.append(vehicle)
    return vehicles