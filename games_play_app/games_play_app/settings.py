"""

1.Execute in terminal -> python manage.py startsapp 'name of the app'
    or in manage.py window(CTRL+ALT+R) -> startsapp 'name of the app'

2.Move the app to the main project dir.
3.Create new py-file(urls.py) in the app folder -> urlpatterns = () ->(must be tuple! or list!).
4.In settings.py add the app in the 'INSTALLED_APPS'.
5.Add path to main project urlpatterns -> path('', include('folder_name.my_app_name.urls')),
6.Run app to see if everything works?.

7.Insert the templates in the projects dir
8.Create more folders with names like -> for example: core/profile/items and move the templates into.

9.Create a new folder inside the main projects dir with name 'staticfiles'.
10.In settings.py add additional setting for static dir ->
                                                                STATICFILES_DIRS = (
                                                                    BASE_DIR / 'staticfiles',
                                                                )

11.test to run one of the staticfiles to test if works fine
    for example-> http://127.0.0.1:8000/static/styles/details.css

12.In settings.py config database
    -THIS CAN BE DONE IN THE END OF THE TASK(django got default db(sqlite3) connected and works same way!
    with postgres settings ->
    https://docs.djangoproject.com/en/4.2/ref/settings/#databases

                                    DATABASES = {
                                        "default": {
                                            "ENGINE": "django.db.backends.postgresql",
                                            "NAME": "name of the database",
                                            "USER": "postgres user",
                                            "PASSWORD": "mypassword",
                                            "HOST": "127.0.0.1",
                                            "PORT": "5432",
                                        }
                                    }

13.Top right corner Database menu -> add new -> Data Source -> PostgreSQL -> fill username and password
    then test the connection and connect.
    This is default and do not change it.
    Must be like this ->
                            Host: localhost
                            Port: 5432
                            URL: jdbc:postgresql://localhost:5432/postgres

    Now right mouse click on the postgres@localhost and create a new database
    with the correct db base from the settings.

14.Now start the app -> may be you will see error ->

            "raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")
            django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module"

15.Need to install "psycopg" or "psycopg2" to work correctly.
16.In terminal execute this -> pip install psycopg2

17.After EVERY! pip install is good to execute-> pip freeze > requiments.txt
    This will create a txt file in your main projects dir
    with name-> 'requiments.txt'
    looking like this ->
                            asgiref==3.6.0
                            Django==4.2.1
                            psycopg2==2.9.6
                            sqlparse==0.4.4
                            tzdata==2023.3

18.You can upgrade your pip -> 'pip install --upgrade pip' (for Windows).

19.Execute in terminal -> "python manage.py migrate"
                            or
    in manage.py window(run it with-> "CTRL+ALT+R") -> "migrate"
    its the same , but in manage.py window you have autocomplete and it`s easier.
    Now you can see in your DB the tables filled in. In "db/public/tables"

20.Run to see if everything works well.Good job :D !

21.Next step is to add urls paths and config with callable func-views.
    for example->

    http://localhost:8000/ - home page
    http://localhost:8000/dashboard/ - dashboard page

    http://localhost:8000/game/create/ - create game page
    http://localhost:8000/game/details/<id>/ - details game page
    http://localhost:8000/game/edit/<id>/ - edit game page
    http://localhost:8000/game/delete/<id>/ - delete game page

    http://localhost:8000/profile/create - create profile page
    http://localhost:8000/profile/details/ - details profile page
    http://localhost:8000/profile/edit/ - edit profile page
    http://localhost:8000/profile/delete/ - delete profile page


    In urls.py looking like this ->

                                urlpatterns = (
                                path('', show_index, name='show index'),
                                path('dashboard/', show_dashboard, name='show dashboard'),

                                path('profile/', include([
                                    path('create/', create_profile, name='create profile'),
                                    path('details/', details_profile, name='details profile'),
                                    path('edit/', edit_profile, name='edit profile'),
                                    path('delete/', delete_profile, name='delete profile'),
                                ])),

                                path('game/', include([
                                    path('create/', create_game, name='create game'),
                                    path('details/<int:pk>/', details_game, name='details game'),
                                    path('edit/<int:pk>/', edit_game, name='edit game'),
                                    path('delete/<int:pk>/', delete_game, name='delete game'),
                                ])),
                            )

    now in views.py ->


        open -> http://localhost:8000/
        -this is without PK/ID->
            def show_index(request):
                return render(request, 'core/home-page.html')


        open -> http://localhost:8000/game/details/1/
        -And this is with PK/ID->
            def details_game(request, pk):
                return render(request, 'game/details-game.html')


    Run to try if working well.
    The pages must visualization without any functionality but rendering.

22.Now it`s time to make a superuser(admin) You can reach the link -> http://127.0.0.1:8000/admin/ , and you will see
    the admin panel for loging into the admin panel, but we still miss the superuser.
    Execute in manage.py->
    createsuperuser and follow the instructions -> fill username,mail,password,repeat password! It`s done.
    Now you can log into admin side.You can create groups and users and giving them permissions and organize all,
    but for now this is enough.

23.Time to fix the templates using inheritance.
    In the template directory create a single file with name -> base.html
    This will be the main/base html who will have the base html elements like navigations and footer
    which is repeating in every html.

    Use this -> to extend the base.html

        {% extends 'base.html' %}
        {% load static %}
        {% block content %}
        {% endblock %}

    and this in base.html to be the parent to all html elements ->
        {% block content %}
        {# information here #}
        {% endblock %}



    base.html must be looking something like this ->
    base.html STARTS HERE ->
                                {% load static %}
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <link rel="stylesheet" href="{% static '/styles/style.css' %}">
                                    <title>GamesPlay</title>
                                </head>

                                <body>
                                <div id="box">
                                    <header>

                                        <!-- Navigation Bar -->
                                        <h1><a class="home" href="{% url 'show index' %}">GamesPlay</a></h1>
                                        <nav>
                                            <!-- if the user has not created a profile -->
                                            <a href="{% url 'create profile' %}">Create Profile</a>
                                            <!-- if the user has created a profile -->
                                            <a href="{% url 'show dashboard' %}">Dashboard</a>
                                            <a href="{% url 'create game' %}">Create Game</a>
                                            <a href="{% url 'details profile' %}">Profile</a>
                                        </nav>
                                    </header>

                                    {% block content %}
                                    {# information here #}
                                    {% endblock %}

                                    <footer>
                                        SoftUni Team 2022. All rights reserved.
                                    </footer>

                                </div>
                                </body>
                                </html>
    base.html ENDS HERE !




    Example of some the html files which must be looking something like this after inheritance ->
        home-page.html STARTS HERE ->

                                    {% extends 'base.html' %}
                                    {% load static %}
                                    {% block content %}

                                    <section id="welcome-world">
                                        <div class="welcome-message">
                                            <h2>ALL new games are</h2>
                                            <h3>Only in GamesPlay</h3>
                                        </div>
                                        <img src="{% static '/images/four_slider_img01.png' %}" alt="hero">
                                    </section>

                                    {% endblock %}

    home-page.html ENDS HERE !

    """

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-s&yb=i*j3&w37cevb_ip&bijzi7sw^&ukc7((x9^u%+d!lqi3r'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'games_play_app.my_web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'games_play_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'games_play_app.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "games_play_db",
        "USER": "postgres",
        "PASSWORD": "doggystyle12345",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
