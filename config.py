import urllib

SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsa.database.windows.net'
SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SQL_SERVER};"
    f"DATABASE={SQL_DATABASE};"
    f"UID={SQL_USER_NAME};"
    f"PWD={SQL_PASSWORD}"
)

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
