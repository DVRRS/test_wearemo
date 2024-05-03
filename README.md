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

Al realizar una solicitud GET a la ruta del microservicio 1, se lee el archivo que se encuentra en GCS, se hace un procesamiento de los datos, quitando los nan y las '' a los datos, posteriomente, se carga la data procesada a una tabla de BigQuery. Esto se hace por medio de una cuenta de servicio asociada a estos dos servicios.

El segundo microservicio es tipo POST cuya ruta es /m2, la cURL y el body se encuentran en .env. Los modulos del segundo microservicio son los siguientes (ignorar el pycache).

![modulo_m2](https://github.com/DVRRS/test_wearemo/assets/69321668/2b6d3228-444a-40ab-9ff6-386bcc695109)

Al realizar una solicitud GET a la ruta del microservicio 2, se lee la tabla que se encuentra en BigQuery, tomando los valores de lat y lon como parametros de la función que se encarga de realizar la solicitud al endpoint de la api de la UK, se realiza un procesamiento del resultado, determinando cual es el codigo postal más cercano teniendo en cuenta el valor '___' del JSON response del endpoint, solamente se obtiene el postcode, este dato se almacena en una nueva tabla en BigQuery junto con las columnas de lat y lon.

Para colocar en funcionamiento el proyecto, se debe correr el siguiente comando: uvicorn main:app --reload para que se mantenga escuchando solicitudes.

Se pueden realizar peticiones al proyecto mediante el docs de FastAPI, y también desde postman.

![docs](https://github.com/DVRRS/test_wearemo/assets/69321668/6f583deb-d4fe-41c2-a653-5fe02b37cd34)



![postman](https://github.com/DVRRS/test_wearemo/assets/69321668/26cc2996-1dd1-4022-9c04-bbfa726020e4)


