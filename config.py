 import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'AZURE_POSTGRESQL_CONNECTIONSTRING'
    ) or 'postgresql://root:root@localhost/my_database'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
