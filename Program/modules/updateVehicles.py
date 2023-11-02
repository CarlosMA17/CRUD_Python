from .addVehicle import addVehicle

def updateVehicles(vehicles, vehicle):
    for vehicleF in vehicles: 
        if vehicleF["model"] == vehicle["model"]:
            vehicles.remove(vehicle)

    vehicles = addVehicle(vehicles)
    return vehicles
