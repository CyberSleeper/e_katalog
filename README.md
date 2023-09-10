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
9. Now you can run the Django server by executing the command below from root directory.
    - Windows:
        ```p
        python manage.py runserver
        ```
    - Unix:
        ```p
        ./manage.py runserver
        ```
</details>

<details>
<summary>Configure the Django project</summary>

1. Create the `main` directory.
    ```p
    python manage.py startapp main
    ```
2. Add `main` directory to the `INSTALLED_APPS` value in `e_katalog/settings.py`.
3. Create a `templates` directory inside `main` directory.
4. Create the `main.html` inside the `templates` directory.
5. Configure the `models.py` inside `main` according to the assignment's favor. For example:
    ```python
    from django.db import models    

    class Item(models.Model):
      name = models.CharField(max_length=255)
      amount = models.IntegerField()
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
    ```
6. Migrate the created model.
    ```p
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Create some render functions in `views.py` inside `main`.
8. Configure the routing at `urls.py`. We can do it directly in `e_katalog/urls.py`, or in `main/urls.py` then include it in `e_katalog/urls.py`.

</details>

<details>
<summary>Push the project to GitHub</summary>
    
1. Create a `.gitignore` file. I used the Django `.gitignore` template from [this](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/) website.
2. Create a new public repository in GitHub named `e_katalog`.
3. Initiate and push the local repository to the Git repository.
    ```p
    git init
    git add -A
    git commit -m "initial commit"
    git branch -M main
    git remote add origin https://github.com/CyberSleeper/e_katalog.git
    git push -u origin main
    ```
    
</details>

<details>
<summary>Deploy the app to Adaptable.io</summary>

1. Create or login to Adaptable account.
2. Create new app by connect to an existing repository, and choose the repository to deploy.
3. Choose the branch to deploy.
4. Select `Python App Template` and then `PostgreSQL`.
5. Select the Python version based on the local Python version and enter below command in `Start Command` field.
    ```p
    python manage.py migrate && gunicorn shopping_list.wsgi
    ```
6. Insert the app name. Note that this value is gonna be the web domain for the app as well.
7. Check the `HTTP Listener on PORT` and deploy the app.

</details>

## <a id="second">What is the relation between `urls.py`, `views.py`, `models.py`, and `html`?</a>

## <a id="third">Why do we use virtual environment?</a>

## <a id="fourth">What is MVC, MVT, MVVM and what is the difference?</a>