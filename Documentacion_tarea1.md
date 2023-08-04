# API de la NASA 
## APIs de la [NASA](https://api.nasa.gov/?ref=apispublicas.com#CAD) consumidas
- Asteroids NeoWS
- Mars Rovers Photos

## Asteroids NeoWS
NeoWs (Near Earth Object Web Service) por sus siglas en Ingles, es el servicio web de detección de objetos cercanos a la Tierra enfocada en asteroides.
Funcionalidades de NeoWs:
- Buscar Asteroides basado en la fecha de mayor cercanía a la tierra.
- Buscar un Asteroide específico usando el id asignado por el equipo JPL de la NASA obteniendo información generalizada del objeto.

Toda la información es tomada del proyecto de Asteriodes del equipo JPL de la NASA. [NASA JPL](http://neo.jpl.nasa.gov/)

## Mars Rover Photos
Esta API es diseñada para recopilar información de imagenes tomadas por los equipos Curiosity, Opportunity y Spirit del proyecto Rovers en Marte y hacerla más fácilmente accesible para otros desarrolladores, educadores y la comunidad científica en general.
Cada Rover tiene su propio grupo de fotos almacenado en la base de datos, las cuales pueden ser accesadas independientemente. Las fotos están organizadas por la fecha Marciana en que fueron tomadas comenzando desde el día de llegada del Rover a Marte el cual sería el día 0.
Las fotos también se pueden accessar por la fecha Terrestre correspondiente.

## Extrayendo fotos por fecha Marciana(sol)
sol se determina por el día de llegada del Rover a Marte siendo el primer día sol=0 y el último el día mas reciente del que se tengan fotografias 
- Ejemplo de endpoint con fecha sol=1000 (1001 día 1001 del Rover en Marte): 
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY

## Extrayendo fotos por fecha terrestre
Se puede también extraer fotos por fecha Terrestre en formato YYYY-MM-DD (Año, mes, día).
- Ejemplo de endpoint con fecha Terrestre de 2015-06-03: 
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-06-03&api_key=DEMO_KEY

DEMO_KEY es una llave para extraer datos de las APIs con ciertas limitaciones en la cantidad de solicitudes que se le pueden hacer al servidor, para usos extensos de datos es necesario solicitar una KEY personal en el sitio web de la [NASA](https://api.nasa.gov/?ref=apispublicas.com#CAD)


## Datos recopilados en el proyecto
### *Asteroids NeoWs*
- Cantidad de total de Asteroides cercanos a la tierra en un rango de fechas Terrestres

### *Mars Rovers*
- Fotos totales tomadas por el Rover Curiosity y Opportunity en un día en específico con fecha terreste.

## Funciones implementadas en la tarea
### getAsteroids():
Esta función hace una solicitud a la API Asteroids NeoWs, necesita un rango de fechas terrestres en formato (YYYY-MM-DD) (Año, mes, día).
El servidor devuelve un Diccionario anidado en el cual el valor asignado a cada llave es del tipo lista, existen diferentes niveles de anidado segun la informacion disponible en el servidor.
La respuesta del servidor contiene informacion de los asteroides detectados dentro del rango de fechas proporcionado por el usuario.
- id del Asteroide
- Diámetro del Asteroide em KM, Millas, pies
- Distancia mas cercana a la tierra dentro del rango de fechas dado por el usuario
- Velocidad del Asteroide entre otros muchos mas.

Dada la gran cantidad de informacion retornada por el servidor en cada solicitud, la función getAsteroids() le muestra al usuario unicamente la cantidad total de asteroides detectados en el rango de fechas proporcionado.
