# Cyber Katalog

https://cyberkatalog.adaptable.app/main 

This is my weekly assignment for Platform Based Programming lecture.

### Jump to
- [Week 02](#week-02)
- [Week 03](#week-03)

## Week 02

### Scope
- [How did I develop this app?](#how-did-i-develop-this-app)
- [What is the relation between Django files?](#what-is-the-relation-between-urlspy-viewspy-modelspy-and-html-file)
- [Why do we use virtual environment?](#why-do-we-use-virtual-environment)
- [What is MVC, MVT, MVVM and what is the difference?](#what-is-mvc-mvt-mvvm-and-what-is-the-difference)

---

### How did I develop this app?

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
<summary>Deploy the project to Adaptable.io</summary>

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

---

### What is the relation between `urls.py`, `views.py`, `models.py`, and `html` file?

![MTV Django Architecture](https://github.com/CyberSleeper/e_katalog/blob/main/media/MVTDjangoArchitecture.png)

Django uses the "MTV Architecture":
- M stands for "Model" which represents the data logic of the app;
- T stands for "Template" which is responsible for representing the data to the user;
- V stands for "View" who manages the flow of data between our models and templates. It also handles user requests,

---

### Why do we use virtual environment?

We use Virtual Environment to restrict our Django project from interfering our other project. Normally we'd have multiple projects in one system and each project will have different package version. To prevent the version conflict, we need virtual environment to keep each package in place.

---

### What is MVC, MVT, MVVM and what is the difference?

#### MVC (Model-View-Controller)

In MVC, we split the code into 3 components where each components has its own specific purposes.

- Model: manages data logic of the app.
- View: manages how the data will be displayed.
- Controller: making the bridge between model and view to by manipulating the models and render the views..

#### MVT (Model-View-Template)

MVT is similar to MVC. The main difference is that the "controller" part is taken care by the framework itself. Templates are basically the HTML code that render the data.

#### MVVM (Model-View-ViewModel)

MVVM uses "ViewModel" which is basically the abstraction of view which wraps the model data. ViewModel is a model that changes to a view according to the command that affects it.

## Week 03

### Scope
- [What is the difference between POST form and GET form in Django?](#what-is-the-difference-between-post-form-and-get-form-in-django)
- [What are the main differences between XML, JSON, and HTML in the context of data delivery?](#what-are-the-main-differences-between-xml-json-and-html-in-the-context-of-data-delivery)
- [Why is JSON often used in data exchange between modern web applications?](#why-is-json-often-used-in-data-exchange-between-modern-web-applications)
- [Explain how you implemented week 02 assignment step-by-step](#explain-how-you-implemented-week-02-assignment-step-by-step)

### What is the difference between POST form and GET form in Django?

The main difference is `POST` form encrypt the form data and send it to server without exposing the data as URL parameter. Meanwhile `GET` form does not encrypt the data and bundles the submitted data as URL parameter. 

POST form
![POST form](https://github.com/CyberSleeper/e_katalog/blob/main/media/POSTForm.png)

GET form
![GET form](https://github.com/CyberSleeper/e_katalog/blob/main/media/GETForm.png)


### What are the main differences between XML, JSON, and HTML in the context of data delivery?

HTML and XML are fairly similar. But they have different purposes. The purpose of XML is organization while the purpose of HTML is presentation. XML does not have pre-defined tags. Therefore we can define our own tags as we like and organize our data with flexibility. Whereas HTML is full of pre-defined tags. Hence, the common case is use HTML to present our data and web structure while XML stores our data in an organized manner.

Same as XML, JSON is used to store and organize our data. The difference is their formatting. JSON enclose their data using curly brackets while XML use HTML-like tags.

XML
```xml
<root>
	<pilot>
		<fruit>apple</fruit>
		<amount>3</amount>
	</pilot>
	<pilot>
		<fruit>longan</fruit>
		<amount>9</amount>
	</pilot>
	<pilot>
		<fruit>durian</fruit>
		<amount />
	</pilot>
	<required>10</required>
</root>
```

JSON
```json
{
    "pilot": [
        {
            "fruit": "apple",
            "amount": 3
        },
        {
            "fruit": "longan",
            "amount": 9
        },
        {
            "fruit": "durian",
            "amount": null
        }
    ],
    "required": 10
}
```


### Why is JSON often used in data exchange between modern web applications?

Most of the time XML is considered inferior because it is relatively hard to maintain the opening and closing tags. JSON is more preferred because of its conciseness and compactness making it faster to parse and generate.

### Explain how you implemented week 02 assignment step-by-step

1. Create a `form` input to add a model object to the previous app. 

    - Create a new file named `forms.py` in `main` directory. We will create the form structure in this file.

        ```python
        from django.forms import ModelForm
        from main.models import Item

        class ItemForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "amount", "description"]
        ```

2. Add 5 `views` to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.

    - Update `main/views.py` and add the required function

3. Create URL routing for each of the views.

    - Update the `main/urls.py` and add the routes based on our `views.py`.

### Result of hitting the endpoint using Thunder Client (Postman-like)

- HTML
![HTML](https://github.com/CyberSleeper/e_katalog/blob/main/media/HTML.png)

- JSON
![JSON](https://github.com/CyberSleeper/e_katalog/blob/main/media/JSON.png)

- JSON_by_id
![JSON_by_id](https://github.com/CyberSleeper/e_katalog/blob/main/media/JSON_by_id.png)

- XML
![XML](https://github.com/CyberSleeper/e_katalog/blob/main/media/XML.png)

- XML_by_id
![XML_by_id](https://github.com/CyberSleeper/e_katalog/blob/main/media/XML_by_id.png)