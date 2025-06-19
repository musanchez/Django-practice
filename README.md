# Django-practice

Este proyecto es una práctica básica con Django.

## Requisitos

- Python 3.8 o superior
- pip
- Virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/Django-practice.git
    cd Django-practice
    ```

2. (Opcional) Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Aplica las migraciones:

    ```bash
    python manage.py migrate
    ```

2. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

3. Accede a la aplicación en [http://localhost:8000](http://localhost:8000)

## Estructura del proyecto

- `manage.py`: Herramienta de administración de Django.
- `app/`: Carpeta principal de la aplicación.
- `requirements.txt`: Dependencias del proyecto.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.