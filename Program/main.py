from modules.addVehicle import addVehicle
from modules.consultVehicle import consultVehicle
from modules.deleteVehicle import deleteVehicle
from modules.updateVehicles import updateVehicles

exit = True
vehicles = []

def switch(case, vehicle, vehicles): 
    match case: 
        case "1": 
            consultVehicle(vehicle)
        case "2": 
            vehicles = addVehicle(vehicles)
        case "3": 
            vehicles = deleteVehicle(vehicles, vehicle)
        case "4": 
            vehicles = updateVehicles(vehicles, vehicle)       
        case "5": 
            return False

while exit:
    vehicle = {}
    option = input("escoja una opcion del programa:\n" +
        "1.- mostrar la base de datos de vehiculos\n" + 
        "2.- añadir un nuevo vehiculo\n" + 
        "3.- eliminar un vehiculo de la base de datos\n" + 
        "4.- actualizar la informacion de un vehiculo\n" +
        "5.- salir del programa\n")
    if option == "1" or option == "3" or option == "4":
        model = input("introduzca el modelo\n")
        for vehicleF in vehicles:
            if model == vehicleF["model"]:
                vehicle = vehicleF


    exit = switch(option, vehicle, vehicles)
   
    if vehicles == []:
        print("la lista de vehiculos esta vacia\n")
    elif option == "1": 
        print("\n")
    else:
        print("\nvehiculos: ", vehicles)
    
    