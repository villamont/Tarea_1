## Prueba con API de la NASA
import requests

##-------------------------Funcion para solicitar asteroides cercanos a la tierra al servidor----------------------------------


#url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY'

#print(url1)

def getAsteroids(fecha_inicial, fecha_final):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='
    start_date=fecha_inicial
    amper='&end_date='
    end_date=fecha_final
    key='&api_key='
    API_KEY='T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd'

    url1 = url + start_date + amper + end_date + key + API_KEY
    getResponse = requests.get(url1)

    
    if getResponse.status_code == 200:
        data = getResponse.json()
        print("Estatus code de la solicitud: ", getResponse.status_code)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #print("tipo de estructura de datos es: ", type(data))
        print("\n\n\n cantidad de asteroides cerca de la tierra para el rango de fechas :",start_date, "al", end_date, "es: ", data["element_count"])
        #for clave in data:
        #    print(clave, '-> ', data[clave], '\n\ntipo de dato', type(clave))

    else:
        print('\nError al realizar la solicitud')

##-------------------------Funcion para solicitar cantidad de photos tomadas por Opportunity---------------------------------


def getOpportunity(fecha):
    part1='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date='
    earth_date=fecha
    key='&api_key=DEMO_KEY'
    url_opportunity=part1 + earth_date + key

    print("\n La url: ", url_opportunity)
    getResponse = requests.get(url_opportunity)
            
    if getResponse.status_code == 200:
        fot_Opportunity = getResponse.json()
        print("XXXXXXXXXXXXXXX--Mostrando cantidad de fotos tomadas por Mars Opportunity segun dias Solares--XXXXXXXXXXXXXXX")
        print("Cantidad total de fotos tomadas por Opportunity:", fot_Opportunity["photos"][0]["rover"]["total_photos"])
        print('Opportunity tomo:', len(fot_Opportunity["photos"]), "fotos el dia", earth_date)
                
    else:
        print('\nError al realizar la solicitud')

##-------------------------Funcion para solicitar cantidad de photos tomadas por curiosity----------------------------------
#url_curiosity="https://api.nasa.gov/mars-photos/api/v1/manifests/Curiosity?api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd&sol=800"


def getCuriosity(date):
    p1='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date='
    earth_date=date
    api_key='&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd'
    url_curiosity= p1 + earth_date + api_key
    
    print("\n La url: ", url_curiosity)
    getResponse = requests.get(url_curiosity)
            
    if getResponse.status_code == 200:
        fot_Curiosity = getResponse.json()
        print("\n\n\nXXXXXXXXXXXXXXX--Mostrando cantidad de fotos tomadas por Mars Curiosity segun fecha dada por el usuario--XXXXXXXXXXXXXXX")
        print("Cantidad total de fotos tomadas por Curiosity:", fot_Curiosity["photos"][0]["rover"]["total_photos"])
        print('Curiosity tomo:', len(fot_Curiosity["photos"]), "fotos el dia", earth_date)    
        

    else:
        print('\nError al realizar la solicitud')





