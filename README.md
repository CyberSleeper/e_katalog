# Cyber Katalog

https://cyberkatalog.adaptable.app/main

This is my 2nd weekly assignment for Platform Based Programming lecture.

## Scope
- [How did I develop this app?](#first)
- [What is the relation between Django files?](#second)
- [Why do we use virtual environment?](#third)
- [What is MVC, MVT, MVVM and what is the difference?](#fourth)

## <a id="first">How did I develop this app?</a>

<details>
<summary >Initiate a new Django project in local directory</summary>

1. Create a new directory named `e_katalog` and navigate to the directory.
    ```p
    mkdir e_katalog
    cd e_katalog
    ```
    
2. Create a new virtual environment.
    ```p
    python -m venv env
    ```
    
3. Activate your virtual environment.
    - Command Prompt
        ```
        env\Scripts\activate.bat
        ```
    - PowerShell
        ```
        ./env/Scripts/Activate.ps1
        ```
    - Unix
        ```
        source env/bin/activate
        ```

4. The `(env)` at the beginning of command line in terminal indicates that the virtual environment is active.

5. Create `requirements.txt` file and add some required dependencies. As instance:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    
6. Install the dependencies by executing the command below. Make sure the virtual environment is still running.
    ```p
    pip install -r requirements.txt
    ```
    
7. Still in the same directory level, create a new project directory named `e_katalog` by executing the command below.
    ```p
    django-admin startproject e_katalog .
    ```

8. For demonstration purpose, allow access from **any** host by setting the `ALLOWED_HOST` value to `["*"]` in `settings.py` file which is located inside the `e_katalog` project from the step before.
    
9. Now you can run the Django server by executing
    - Windows:
        ```
        python manage.py runserver
        ```
    - Unix:
        ```
        ./manage.py runserver
        ```
</details>

## <a id="second">What is the relation between `urls.py`, `views.py`, `models.py`, and `html`?</a>

## <a id="third">Why do we use virtual environment?</a>

## <a id="fourth">What is MVC, MVT, MVVM and what is the difference?</a>