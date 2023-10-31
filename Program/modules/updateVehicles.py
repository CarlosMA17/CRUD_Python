from .deleteVehicle import deleteVehicle 
from .addVehicle import addVehicle

def updateVehicles(vehicles, vehicleModel):
    for vehicle in vehicles: 
        if vehicle["model"] == vehicleModel:
            vehicles.remove(vehicle)

    vehicles = addVehicle(vehicles)
    return vehicles
