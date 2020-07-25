Proyecto aplicación web control CRIPTOMONEDAS

## Instalación

1. Instalar Entorno Virtual y Flask

```
python3 -m venv ven
```
2. Habilitar el entorno virtual en Terminal
```
. ven/bin/activate
```
Aparecerá (venv) delante del cursor como indicativo de virtual environment

3. Instalar Flask

```
pip install Flask
```

4. Instalar dependencias

```
pip install -r requirements.txt
```

5. Exportar para visualización

```
export FLASK_APP=index
```
```
export FLASK_ENV=development
```

6. Ejecutar run en Virtual Environment

```
flask run
```