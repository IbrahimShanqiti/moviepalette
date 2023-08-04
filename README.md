# What is it

Movie Palette!

## Description

...

### Local installation

Use pyenv and pipenv
Use pyenv version 3.10.x

```
pipenv shell
pipenv install 
```

### Local Development: 

```
export FLASK_APP=app.py
python -m flask run
```

### To run: 

```
docker build . -t moviepalette
docker run --init -p 5000:5000 -it moviepalette:latest
```