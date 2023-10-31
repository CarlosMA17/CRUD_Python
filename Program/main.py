from modules.addVehicle import addVehicle
from modules.consultVehicle import consultVehicle
from modules.deleteVehicle import deleteVehicle
from modules.updateVehicles import updateVehicles

vehicle1 = {
    "brand" : "BMW",
    "model" : "e36",
    "year" : "1989"
}
vehicles = [vehicle1]
print(vehicles)


vehicles = addVehicle(vehicles) # añadir un elemento 
for vehicle in vehicles:
    consultVehicle(vehicle)

vehicles = deleteVehicle(vehicles, "e46") # eliminar un elemento
for vehicle in vehicles:
    consultVehicle(vehicle)

vehicles = updateVehicles(vehicles, "e36") # actualizar un elemento
for vehicle in vehicles:
    consultVehicle(vehicle)