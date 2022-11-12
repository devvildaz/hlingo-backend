from mongoengine import connect, disconnect
from ..schemas.AppUser import AppUser
from ..settings import settings

DEFAULT_CONNECTION_NAME = connect(host=(
        f'mongodb+srv://{settings.db_user}:{settings.db_password}'
        f'@{settings.db_host}/{settings.db_name}'
        '?authSource=admin'
        '&connectTimeoutMS=60000'
    ))
    
def init_database():
    connect(host=(
        f'mongodb+srv://{settings.db_user}:{settings.db_password}'
        f'@{settings.db_host}/{settings.db_name}'
        '?authSource=admin'
        '&connectTimeoutMS=60000'
    ))
def shutdown_database():
    disconnect()