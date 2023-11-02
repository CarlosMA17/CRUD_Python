def deleteVehicle(vehicles, vehicle):

    comparationList = vehicles.copy()

    for vehicleF in vehicles: 
        if vehicleF["model"] == vehicle["model"]:
            vehicles.remove(vehicleF)
            print("se ha borrado el vehiculo")

    if len(comparationList) == len(vehicles):
        print(len(comparationList), len(vehicles))
        print("no se encontro el modelo")

    return vehicles