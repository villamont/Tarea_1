##Main program para el modulo API_NASA

import API_NASA as NASA
print("""
Este programa te muestra la siguiente informacion\n - La cantidad de fotografias tomadas en el proyecto Mars Rover de la NASA en un dia en especifico, incluyendo las sondas Curiosity y Oportunity. \n - Cantidad de Asteroides cercanos a la tierra en un rango de fechas establecida por el usuario
""")

#Salir=' '
def get_urs_options():
    sal=' '
    while sal != 'Salir':   
        
        try:
            
            opcion=int(input("""
Por favor escoja la informacion que desea obtener en el siguiente menu:
    1 --> Fotografias tomadas por sonda Oportunity en un dia en especifico.
    2 --> Fotografias tomadas por sonda Curiosity en un dia en especifico.
    3 --> Asteroides cercanos a la tierra en un rango de fechas
    4 --> Salir
    ===>  """))
            if opcion == 1:
                fecha=str(input("Por favor ingrese la fecha en formato YYYY-MM-DD >>> escoja una fecha entre 2004-01-26 al 2018-06-07 <<<\n"))
                NASA.getOpportunity(fecha)

            elif opcion == 2: 
                date=str(input("Por favor ingrese la fecha en formato YYYY-MM-DD >>> escoja una fecha entre 2014-10-01  a fecha actual (2023-08-04) <<<\n"))
                NASA.getCuriosity(date)

            elif opcion == 3: 
                fecha_ini=str(input("\n Ingrese el rango de fechas (maximo de 5 dias) entre 1900-01-01 a la fecha actual (2023-08-04) \nPor favor ingrese una fecha inicial\n"))
                fecha_fin=str(input("\nPor favor ingrese una fecha final\n"))
                NASA.getAsteroids(fecha_ini, fecha_fin)

            elif opcion == 4:
                sal="Salir"  
                print("Esperamos haya disfrutado los datos del Proyecto Asteroids NeoWS y MARS Rover")
            
        except ValueError:
            print("\nOpcion no valida, por favor ingresa un valor valido") 

    
    


if __name__ == '__main__':
    get_urs_options()
    




