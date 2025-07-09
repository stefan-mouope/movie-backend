import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
load_dotenv()


# --- BASE DIR ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECRET KEY ---
SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret")

# --- DEBUG MODE ---
DEBUG = os.environ.get("DEBUG", "False") == "True"

# --- ALLOWED HOSTS ---
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME, "localhost"]
else:
    ALLOWED_HOSTS = ["localhost"]

# --- INSTALLED APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps tiers
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',

    # App locale
    'movies',
]

# --- CORS ---
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://movie-frontend.onrender.com",  # À ajuster selon ton domaine Render Frontend
    "http://localhost:5173",
]

# --- REST FRAMEWORK ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Pour servir les fichiers statiques
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- ROOT CONFIG ---
ROOT_URLCONF = 'movie_recommender.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Ajoute ici tes dossiers de templates si nécessaire
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movie_recommender.wsgi.application'

# --- DATABASE ---
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL", "sqlite:///" + str(BASE_DIR / "db.sqlite3")),
        conn_max_age=600,
    )
}

# --- PASSWORD VALIDATORS ---
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

# --- LOCALISATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- DEFAULT PRIMARY KEY ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
