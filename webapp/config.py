"""Configure application settings such as the database URI, secret key, etc."""

# See https://flask-appbuilder.readthedocs.io/en/latest/config.html


SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://profs@data.cs.jmu.edu/profs"

SECRET_KEY = "c46096d07cfae2ef311332eb98bc8336acaacf162427122b285ceb388a1cade1"

AUTH_TYPE = 1  # Database style (user/password)

APP_NAME = "madiSTEM Workshop Management"

APP_THEME = "readable.css"
