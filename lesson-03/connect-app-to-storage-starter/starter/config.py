import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'yross-sql-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'yross-sql-database-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
   # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'    
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'yrossaccount01'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'HXhyga7DhdLE45THw5Hl6rTqdeuKJs/0BP0wtor+0c7uOtlgGyqk7Zd987xsyQn0I7Nuki8qLTbONhu2YxZppQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
