from .deleteVehicle import deleteVehicle 
from .addVehicle import addVehicle

def updateVehicles(vehicles, vehicleModel):
    for vehicle in vehicles: 
        if vehicle["model"] == vehicleModel:
            vehicles = deleteVehicle(vehicles, vehicle["model"])

    vehicles = addVehicle(vehicles)
    return vehicles
