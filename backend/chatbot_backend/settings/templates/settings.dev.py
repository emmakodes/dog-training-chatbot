# mypy: ignore-errors

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yq1#*!e9*u39z4ixm9sq_u!$7md)!t6gdnnyi9op#23e0u%o16"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

MIDDLEWARE += ('backend.backend.middleware.LoggingMiddleware',)  # type: ignore
LOGGING['formatters']['colored'] = { # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s', # type: ignore
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
