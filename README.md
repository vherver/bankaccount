
![GitHub Actions](https://github.com/vherver/bankaccount/workflows/django/badge.svg)


Este proyecto tiene la capacidad de recibir un archivo csv para crear una cuenta y sus transacciones, una vez procesadas y almacenadas en la base de datos enviara un resumen de todas las transacciones existentes en la cuenta (no solo las enviadas en el csv)

El csv deberá estar conformado de la siguiente manera


|account|date|amount|
| :- | :- | :- |
|vicherver@gmail.com|2023/10/20|-50.52|
|hugoherver@gmail.com|2023/10/20|+65.30|
|hugoherver@gmail.com|2023/10/20|-96.60|

Consideraciones

- account deberá ser un email valido (en formato), de lo contrario no será procesada la transacción (estas serán indicadas como un warning).
- pueden incluirse más de un correo, serán procesadas y enviadas a los distintos destinatarios
- date deberá estar en el formato AAAA/MM/DD, de lo contrario no será procesada la transacción (estas serán indicadas como un warning).

Podra encontrar el ejemplo de [csv valido](https://github.com/vherver/bankaccount/blob/main/example.csv)

La distribución de correos electrónicos se hace por medio de sendgrid utilizando templates dinámicos, 
podrá encontrar [el template](https://github.com/vherver/bankaccount/blob/main/backaccount/templates/sendgrid/account_balance.html).


Levantar proyecto en local

El proyecto está empaquetado en docker para levantarlo en local, una vez clonado el repositorio:

docker-compose build

```
docker-compose build
```

```
docker-compose up
```

El proyecto correrá en localhost:8000

