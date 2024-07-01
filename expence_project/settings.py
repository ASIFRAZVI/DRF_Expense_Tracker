from dotenv import load_dotenv
from pathlib import Path, os
from .DB import DB
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

#load env
dev_Key = os.getenv("dev_key")
print(dev_Key)

SECRET_KEY = 'django-insecure-bsqmga(50e6xnogy2)r%)^d$1h8oi$3khz#ol^jy^1rwelj=^h'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "authentication_app",
    "crud_app",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'expence_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'expence_project.wsgi.application'

db_type= os.getenv("DB_TYPE")
print(db_type)

if db_type=="development":
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("Dev_DB_ENGINE"),
            'NAME': os.getenv("Dev_DB_NAME"),
            'USER': os.getenv("Dev_DB_USER"),
            'PASSWORD': os.getenv("Dev_DB_PASSWORD"),
            'HOST': os.getenv("Dev_DB_HOST"),
            'PORT': os.getenv("Dev_DB_PORT"),
        },
        'expense_db_dev': {
            'ENGINE': os.getenv("expense_db_ENGINE"),
            'NAME': os.getenv("expense_db_NAME"),
            'USER': os.getenv("expense_db_USER"),
            'PASSWORD': os.getenv("expense_db_PASSWORD"),
            'HOST': os.getenv("expense_db_HOST"),
            'PORT': os.getenv("expense_db_PORT"),
    },
    }
    
elif db_type=="production":
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("Pro_DB_ENGINE"),
            'NAME': os.getenv("Pro_DB_NAME"),
            'USER': os.getenv("Pro_DB_USER"),
            'PASSWORD': os.getenv("Pro_DB_PASSWORD"),
            'HOST': os.getenv("Pro_DB_HOST"),
            'PORT': os.getenv("Pro_DB_PORT"),
        },
    }

#use DB Package insted of normal settings
# DATABASES = {
#     'default': DB.get_db_settings(),
# }

# or DB


# db routers for multiple db #this is for expense crud app
DATABASE_ROUTERS = [
    'crud_app.db_router.ExpenseRouter',
]

#specify manually which model using for authentication
AUTH_USER_MODEL = 'authentication_app.CustomUser'


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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
