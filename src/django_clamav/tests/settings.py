DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


INSTALLED_APPS = [
    "django_clamav",
]

SECRET_KEY = "Anti virus scanner"

LANGUAGE_CODE = "en"
