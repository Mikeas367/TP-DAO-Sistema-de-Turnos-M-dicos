# Estructura del proyecto
* /controllers
    * Carpeta que contiene los distintos controladores para los casos de uso.
* /interfaces
    * Carpeta que contiene interfaces abstractas, como es el caso de la IRepository, que permite la inversion de dependencia entre las capas de persistencia y dominio
* /models
    * Contiene los modelos del dominio del problema
* /repositories
    * tiene las intancias concretas de las interfaces
* /routes
    * Tiene los distintos paths para hacer solicitudes al back
* /schemas
    * Contiene esquemas de los modelos del dominio lo que le permite a fastApi validar tipos y tener en cuenta que es lo que le llega desde el exterior
* app.py
    * aplicacion principal
* database.py
    * clase que se encarga de la coneccion a la db y la creacion de la misma

## Dependencias para el proyecto
para el proyecto estamos utilizando fastApi y uvicorn. Para instalar estas dependencias utilizamos el siguiente comando:
```
python -m pip install fastapi uvicorn
```

## Iniciar el proyecto

```
python -m uvicorn app:app --reload
```