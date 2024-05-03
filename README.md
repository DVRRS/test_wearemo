# test_wearemo

Arquitectura

![architecture](https://github.com/DVRRS/test_wearemo/assets/69321668/c66c54c5-b3b3-4413-a2f4-b2730e123403)

Se usó FastAPI para el backend, para aprovechar sus ventajas ___

La aplicación se compone de los siguientes modulos: 

![modulos](https://github.com/DVRRS/test_wearemo/assets/69321668/ee6845eb-a9c5-49e8-9a4d-46cd45789030)

En el archivo .env se encuentran las variables de entorno.

A cada microservicio se le asigna una ruta en especifico, siendo M1 la del primer microservicio, M2 la del segundo microservicio. 

El primer microservicio es tipo GET cuya ruta es /m1, la cURL se encuentra en .env. El modulo del microservicio es el siguiente:

![modulo_m1](https://github.com/DVRRS/test_wearemo/assets/69321668/6c871afd-e48d-4601-ad50-6f594d19ee55)

El segundo microservicio es tipo POST cuya ruta es /m2, la cURL y el body se encuentran en .env. Los modulos del segundo microservicio son los siguientes (ignorar el pycache).

![modulo_m2](https://github.com/DVRRS/test_wearemo/assets/69321668/2b6d3228-444a-40ab-9ff6-386bcc695109)

Para colocar en funcionamiento el proyecto, se debe correr el siguiente comando: uvicorn main:app --reload para que se mantenga escuchando solicitudes.

Se pueden realizar peticiones al proyecto mediante el docs de FastAPI, y también desde postman.

** colocar imagen de docs

** colocar imagen de postman


