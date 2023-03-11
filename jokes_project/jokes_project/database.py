from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE = {
    'default': {
        'ENGINE': config['ENGINE'],
        'NAME': config['NAME'],
        'PASSWORD': config['PASSWORD'],
        'USER': config['USER'],
        'HOST': config['HOST'],
        'PORT': config['PORT'],
    },
    
    'OPTIONS': {
        'driver': 'ODBC Driver 17 for SQL Server'
    }
}