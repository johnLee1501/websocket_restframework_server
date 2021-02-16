# Api Rest con implementación de websocket

Aplicación desarrollada con Django Channels Rest Framework que envía mensajes al cliente sobre todas las operaciones CRUD realizadas a través del ORM de Django en un modelo.

### Algunas caracteristicas principales: 

- Interfaz Swagger para realizar operaciones CRUD
- Servidor WebSocket para enviar al cliente todos los cambios realizados en el modelo User


## Getting Started

Estas instrucciones te proporcionarán una copia del proyecto en funcionamiento en tu máquina local con fines de desarrollo y prueba.

### Prerrequisito

Si quieres probar, necesitarás estos requisitos previos

```
Python > 3.6
```

### Instalación

Primero, clona el proyecto en tu computadora

```
git clone https://github.com/johnLee1501/websocket_restframework_server.git
```

luego, cree un entorno virtual para el proyecto, puede usar virtualenvwrapper-win si su sistema operativo es Windows

```
pip install virtualenvwrapper-win
mkvirtualenv <nombre_del_entorno>
```

después de eso, instale los paquetes en requirements.txt para asegurarse de tener todo lo necesario

```
pip install -r requirements.txt
```

finalmente, realice las migraciones correspondientes al modelo

```
py manage.py makemigrations
py manage.py migrate
```

Listo! ya puedes ejecutarlo

```
py manage.py runserver
```

Ingresa a localhost:8000/admin o localhost:8000/swagger y explore

Nota: necesitará credenciales de usuario para acceder al panel de administración de Django y para poder hacer uso de los diferentes endpoints de Swagger, asegúrese de crear un usuario con

```
py manage.py createusersuperuser
```

## Autor

* **John Vega**

## Screenshots
