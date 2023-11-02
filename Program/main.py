from modules.addVehicle import addVehicle
from modules.consultVehicle import consultVehicle
from modules.deleteVehicle import deleteVehicle
from modules.updateVehicles import updateVehicles

exit = True
vehicles = []

def switch(case, vehicle, vehicles): 
    match case: 
        case "1": 
            for vehicle in vehicles:
                consultVehicle(vehicle)
            return True
        case "2": 
            vehicles = addVehicle(vehicles)
            return True
        case "3": 
            vehicles = deleteVehicle(vehicles, vehicle)
            return True
        case "4": 
            vehicles = updateVehicles(vehicles, vehicle) 
            return True      
        case "5": 
            return False
        case _:
            print("no es valido")

while exit:
    vehicle = {}
    option = input("escoja una opcion del programa:\n" +
        "1.- mostrar la base de datos de vehiculos\n" + 
        "2.- añadir un nuevo vehiculo\n" + 
        "3.- eliminar un vehiculo de la base de datos\n" + 
        "4.- actualizar la informacion de un vehiculo\n" +
        "5.- salir del programa\n")
    if option == "3" or option == "4":
        brand = input("introduzca la marca\n")
        model = input("introduzca el modelo\n")
        year = input("introduzca el año\n")
        for vehicleF in vehicles:
            if brand == vehicleF["brand"] and model == vehicleF["model"] and year == vehicleF["year"]:
                    vehicle = vehicleF


    exit = switch(option, vehicle, vehicles)
    if exit == True:
        if vehicles == []:
            print("la lista de vehiculos esta vacia\n")
        elif option == "1": 
            print("\n")
        else:
            print("\nvehiculos: ", vehicles)
    else:
        print("cerrando el programa...")
    
    