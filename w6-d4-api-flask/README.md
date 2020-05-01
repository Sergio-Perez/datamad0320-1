# Flask API

## Run the server

`./runServer.sh`

Please check before running that you have execution permissions `chmod +x runServer.sh`

## Deploy a heroku

0. Crear una cuenta en heroku y una nueva app
1. Instalar `heroku-cli`
    - Hacer login en heroku `$ heroku login`
2. Subir la imagen a heroku con `$ heroku container:push -a datamad0320 web`
3. Desplegar la app en heroku con `$ heroku container:release -a datamad0320 web`

Help:
- Debugar la app en heroku viendo los logs `$ heroku logs -a datamad0320`


## Preparar MongoDB Atlas

1. Crear cuenta en [https://cloud.mongodb.com/]
2. Crear un cluster
3. Crear un usuario con acceso a escritura a la bbdd
4. Configurar la variable de entorno `DBURL` en heroku (settings/config_vars) apuntando a la url de `MongoDB Atlas` 
   1. `mongodb+srv://<username>:<password>@cluster0-2ak5e.mongodb.net/<nombre_bbdd_que_tu_quieras>`
5. Sincronizar la BBDD local con la BBDD en Mongodb atlas usando el script `$ bash syncDb.sh`


## Refs
- [https://cloud.mongodb.com/]
- [https://flask.palletsprojects.com/en/1.1.x/]
- [https://devcenter.heroku.com/articles/build-docker-images-heroku-yml]
