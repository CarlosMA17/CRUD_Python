def deleteVehicle(vehicles, vehicleModel) :
    comparationList = vehicles.copy()
    for vehicle in vehicles: 
        if vehicle["model"] == vehicleModel:
            vehicles.remove(vehicle)
            print("se ha borrado el vehiculo")

    if len(comparationList) == len(vehicles):
        print(len(comparationList), len(vehicles))
        print("no se encontro el modelo")

    return vehicles