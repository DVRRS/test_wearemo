# test_wearemo

Arquitectura

![architecture](https://github.com/DVRRS/test_wearemo/assets/69321668/c66c54c5-b3b3-4413-a2f4-b2730e123403)

Se usó FastAPI para el backend, para aprovechar sus ventajas, tales como: generar la __documentación automática__ para facilitar el uso de la API, que permite la __asincronía__ para mejorar el rendimiendo y dado el poco tiempo, permite un __desarrollo rápido__ con la detección de errores en tiempo de compilación.

La aplicación se compone de los siguientes modulos: 

![modulos](https://github.com/DVRRS/test_wearemo/assets/69321668/ee6845eb-a9c5-49e8-9a4d-46cd45789030)

En el archivo .env se encuentran las variables de entorno, se comparte en el correo.

A cada microservicio se le asigna una ruta en especifico, siendo M1 la del primer microservicio, M2 la del segundo microservicio. 

**El primer microservicio es tipo GET cuya ruta es /m1**, la cURL se encuentra en .env. 
El modulo del microservicio es el siguiente:

![modulo_m1](https://github.com/DVRRS/test_wearemo/assets/69321668/6c871afd-e48d-4601-ad50-6f594d19ee55)

Al realizar una solicitud GET a la ruta del microservicio 1, se lee el archivo que se encuentra en GCS, se hace un procesamiento de los datos, quitando los nan y las "''" a los datos, posteriomente, se carga la data procesada a una tabla de BigQuery, relacionando un id único a cada coordenada. Esto se hace por medio de una cuenta de servicio asociada a estos dos servicios.
_Obteniendo como resultado en BigQuery_

![bqm1](https://github.com/DVRRS/test_wearemo/assets/69321668/50f464b5-ac2b-4206-a33f-93b61452d69b)


**El segundo microservicio es tipo POST cuya ruta es /m2**, la cURL y el body se encuentran en .env. Los modulos del segundo microservicio son los siguientes (ignorar el pycache).

![modulo_m2](https://github.com/DVRRS/test_wearemo/assets/69321668/2b6d3228-444a-40ab-9ff6-386bcc695109)

Al realizar una solicitud GET a la ruta del microservicio 2, se lee la tabla que se encuentra en BigQuery, tomando los valores de lat y lon como parámetros de la función que se encarga de realizar la solicitud al endpoint (getPostcode) de la api de la UK, se realiza un procesamiento del resultado, determinando cual es el código postal más cercano teniendo en cuenta el valor 'distance' del JSON response del endpoint, solamente se obtiene el postcode, este dato se almacena en una nueva tabla en BigQuery junto con las columnas de id, lat y lon.
_Obteniendo como resultado en BigQuery_

![bqm2](https://github.com/DVRRS/test_wearemo/assets/69321668/b08007ab-81da-4af7-9f0e-bc986e713264)

**FUNCIONAMIENTO**
Para colocar en funcionamiento el proyecto, se debe correr el siguiente comando: uvicorn main:app --reload para que se mantenga escuchando solicitudes.

Se pueden realizar peticiones al proyecto mediante el docs de FastAPI, y también desde postman.

![docs](https://github.com/DVRRS/test_wearemo/assets/69321668/6f583deb-d4fe-41c2-a653-5fe02b37cd34)

Para realizar consultas al microservicio 1, se debe agregar la información del bucket y blob, donde se encuentra almacenado el archivo del proyecto. Esta información se comparte en el correo.

![m1_1](https://github.com/DVRRS/test_wearemo/assets/69321668/95f13301-ef08-4899-9c9c-7f132b915c08)

Una vez agregada la información requerida, se obtiene como resultado:

![responsem1](https://github.com/DVRRS/test_wearemo/assets/69321668/99ce2c48-eb2b-46fd-8bd8-b480451f7d84)

Para realizar consultas al microservicio 2, se debe realizar la solicitud GET primero o que ya exista la tabla con los datos de latitud y longitud; adicionalmente, la información de start y end que son parametros que dan la posibilidad al usuario de iterar las coordenadas que desea por medio del id asociado a cada coordenada.

![m2_2](https://github.com/DVRRS/test_wearemo/assets/69321668/826107c5-2d50-4b23-abe8-a9816e9e03e2)

Al realizar la solicitud, el microservicio responde:

![m2_3](https://github.com/DVRRS/test_wearemo/assets/69321668/c2114423-dd81-42bf-b8c9-831183874b00)

Adicionalmente, se tienen las siguientes impresiones en pantalla, que nos indica si las coordenas consultadas generaron un postcode y si se subieron a bigquery.

![m2_4](https://github.com/DVRRS/test_wearemo/assets/69321668/c2a453cd-9f81-4575-8688-d8e3ffe02adb)

Para Postman se envían las cURL para ser importadas.

![postman](https://github.com/DVRRS/test_wearemo/assets/69321668/26cc2996-1dd1-4022-9c04-bbfa726020e4)


**PUNTOS A MEJORAR:**
Desarrollo del middlewares que evite que el proyecto se dañe cuando el usuario agrega los datos de solicitud de manera erronea (si llega a pasar, con guardar cualquier archivo (sin modificar nada) el proyecto se reactiva).
Desarrollo del manejo de intentos, ya que en ocasiones el servicio arroja que no encuentra la tabla, esto se soluciona realizando una petición nuevamente (reintento).
Desarrollo de un código que permita una consulta más óptima en recursos y tiempo.



