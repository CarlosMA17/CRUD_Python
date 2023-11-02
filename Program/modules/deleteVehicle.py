def deleteVehicle(vehicles, vehicle):

    '''
    A copy of the list is made to verify in the future that the vehicle has been removed.
    '''

    comparationList = vehicles.copy()
    
    '''
    The vehicle is deleted and if the length of the two lists is the same,
    the vehicle has not been found.
    '''

    vehicles.remove(vehicle)
    print("se ha borrado el vehiculo")

    if len(comparationList) == len(vehicles):
        print("no se encontro el modelo")

    return vehicles