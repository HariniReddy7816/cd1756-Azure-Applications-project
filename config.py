import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING')

    # SQL Server Settings
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    # ------------------------------
    # FIXED SQLALCHEMY CONNECTION STRING
    # ------------------------------
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}"
        f"@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Azure AD Auth
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
