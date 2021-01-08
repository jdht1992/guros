## Guros Demo
Proyecto que detecta si una persona tiene diferencias genéticas basándose en
su secuencia de ADN.

### Módulos incluidos
Domain
```sh
 http://ec2-3-138-107-27.us-east-2.czompute.amazonaws.com
```

 - 1.- API en donde se pueda detectar si existe mutación enviando la secuencia de ADN
mediante un JSON, de ser verdadero retornara un status 200 de los contrario un status 403:

endpoint 
 ```sh
/api/mutation/
```
PayLoad
 ```sh
{
    "dna":["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
}
```


- 2.-  API que retorna un JSON con las estadísticas de las verificaciones de ADN:

endpoint 
 ```sh
/api/stats/
```
PayLoad
 ```sh
{
    "count_mutations": 40,
    "count_no_mutation": 100,
    "ratio": 0.4
}
```

 ### Requerimientos
 - Docker
 - Docker Compose
 

 ### Instalar Docker
 El primer paso es instalar la aplicación Docker de escritorio para su máquina local:
 - [Docker para Mac](https://docs.docker.com/docker-for-mac/install/)
 - [Docker para Windows](https://docs.docker.com/docker-for-windows/install/)
 - [Docker para Linux](https://docs.docker.com/engine/install/#server)

 Docker Compose es una herramienta adicional que se incluye automáticamente con las descargas de Docker para Mac y Windows. Sin embargo, si está en Linux, deberá agregarlo manualmente. Puede hacer esto ejecutando el comando sudo pip install docker-compose una vez completada la instalación de Docker.


### Instalacion.

Clonar el proyecto
```sh
git clone https://github.com/jdht1992/guros.git
```

Dentro del folder de guros ejecutar el comando docker-compose up
```sh
cd guros
docker-compose up
```

### Ejecutar proyecto.

Para ejecutar las migraciones, correr el comando.
```sh
docker-compose exec web python manage.py migrate
```
