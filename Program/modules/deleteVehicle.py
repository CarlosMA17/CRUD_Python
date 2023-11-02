def deleteVehicle(vehicles, vehicle):

    comparationList = vehicles.copy()

    vehicles.remove(vehicle)
    print("se ha borrado el vehiculo")

    if len(comparationList) == len(vehicles):
        print("no se encontro el modelo")

    return vehicles