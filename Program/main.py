from modules.addVehicle import addVehicle
from modules.consultVehicle import consultVehicle
from modules.deleteVehicle import deleteVehicle
from modules.updateVehicles import updateVehicles

vehicle1 = {
    "brand" : "BMW",
    "model" : "e36",
    "year" : "1989"
}

exit = False
    


def switch(case, vehicle):
    switch_dict = {
        '1': consultVehicle(vehicles),
        '2': addVehicle(vehicles),
        '3': deleteVehicle(vehicles, vehicle),
        '4': updateVehicles(vehicles, vehicle),        
        '5': exit
    } 
vehicles = [vehicle1]
print(vehicles)


option = input("bienvenido al progarma, escoja una opcion:\n" +
      "1.- mostrar la base de datos de vehiculos\n" + 
      "2.- añadir un nuevo vehiculo\n" + 
      "3.- eliminar un vehiculo de la base de datos\n" + 
      "4.- actualizar la informacion de un vehiculo\n" +
      "5.- salir del programa")

switch(option)