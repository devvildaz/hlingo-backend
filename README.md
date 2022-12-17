Proyecto que contiene la aplicacion desarrollada en FastAPI la cual se encargara en la administacion de la base de datos 

### Requisitos previos
Tener un entorno virtual de Python 3.9
(Opcional) Tener instalado Docker

# Instalacion y ejecucion del proyecto

### Instalacion de paquetes

```
$ pip install -r requirements.txt
```

### Ejecucion de la aplicacion FastAPI con uvicorn para entorno de desarrollo

```
$ uvicorn main:app --reload
```
### Ejecucion de la aplicacion FastAPI con uvicorn para entorno de producción

```
$ uvicorn main:app --host 0.0.0.0 --port 8000
```

### Ejecucion de la aplicacion en Docker
Descomentar la linea del archivo Dockerfile
```
#COPY ./.env ./.env
```
y ejecutar
```
$ docker build . -t <nombre-imagen>:<tag>
```
```
$ docker run . -t <nombre-imagen>:<tag>
```
```
$ docker run -it -p 8000:8000 --name <nombre-container> <nombre-imagen>:<tag>
```
