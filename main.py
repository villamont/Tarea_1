##Main program para el modulo API_NASA

import API_NASA as NASA
print("""
Este programa te muestra informacion de la cantidad de fotografias tomadas en el proyecto Mars Rover de la NASA
en un dia en especifico, incluyendo las sondas Curiosity y Oportunity, tambien muestra la informacion de Asteroides cercanos a la tierra.
en un rango de fechas establecida por el usuario
""")

#Salir=' '
def get_urs_options():
    sal=' '
    while sal != 'Salir':   
        
        try:
            
            opcion=int(input("""
            Por favor escoja la informacion que desea obtener en el siguiente menu,\n de lo contrario escoja la opcion 4 para salir
            1 --> Fotografias tomadas por sonda Oportunity del Proyecto Mars Rover
            2 --> Fotografias tomadas por sonda Curiosity del Proyecto Mars Rover
            3 --> Asteroides cercanos a la tierra en un rango de fechas
            4 --> Salir
            """))
            if opcion == 1:
                fecha=str(input("Por favor ingrese la fecha en formato YYYY-MM-DD que desea conocer la cantidad de fotografias tomadas pro Mar Opportunity\n"))
                NASA.getOpportunity(fecha)

            elif opcion == 2: 
                date=str(input("Por favor ingrese la fecha en formato YYYY-MM-DD que desea conocer la cantidad de fotografias tomadas pro Mar Curiosity\n"))
                NASA.getCuriosity(date)

            elif opcion == 3: 
                fecha_ini=str(input("\n Ingrese el rango de fechas solicitado a continuacion \nPor favor ingrese una fecha inicial\n"))
                fecha_fin=str(input("\nPor favor ingrese una fecha final\n"))
                NASA.getAsteroids(fecha_ini, fecha_fin)

            elif opcion == 4:
                sal="Salir"  
                print("Esperamos haya disfrutado los datos del Proyecto NASA y MARS Rover")
            
        except ValueError:
            print("\nOpcion no valida, por favor ingresa un valor valido") 

    
    


if __name__ == '__main__':
    get_urs_options()
    




