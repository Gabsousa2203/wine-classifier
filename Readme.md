# Wine Classifier
Este es el repositorio de la inteligencia artificial entrenada para poder calificar la calidad del vino

## Desarrolladores
<table align="center">
    <tbody>
        <tr>
            <td align="center"><a href="https://github.com/MayoJuanDavid" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/102425852?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Juan David Mayo</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
            <td align="center"><a href="https://github.com/Cris27M" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/145819828?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Cristhian Mendes</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
            <td align="center"><a href="https://github.com/jamer1215" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/145820049?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Jamal Mohamad</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
            <td align="center"><a href="https://github.com/Gabsousa2203" rel="nofollow"><img src="https://avatars.githubusercontent.com/u/147444025?v=4" width="150px;" alt="" style="max-width:100%;"><br><sub><b>Gabriel De Sousa</b></sub></a><br><a href="" title="Commits"><g-emoji class="g-emoji" alias="book" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4d6.png">📖</g-emoji></a></td>
        </tr>
    </tbody>
</table>

## Creacion del Ambiente Virtual

```bash
$ python -m venv venv

#Activar
$ venv\Scripts\activate

#Desactivar (opcional)
$ deactivate

#Instalar dependencias
$ pip install -r requirements.txt
```

## Correr la app

```bash
$ uvicorn controller:app --reload
```

## Swagger

Cuando en la terminal aparezca 

```bash
INFO:     Will watch for changes in these directories: ['D:\\Universidad\\IA\\wine-classifier']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14256] using WatchFiles
INFO:     Started server process [10416]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Entrar al navegador de su preferencia y escribir

```bash
http://localhost:8000/docs
```