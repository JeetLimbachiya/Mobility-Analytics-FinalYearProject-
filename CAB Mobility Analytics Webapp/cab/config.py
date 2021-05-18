import os

# Base dir path 
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Base_dir_input = PATH + '/'

# Credential function
def config():
    credentials = {
        # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
        'BASE_DIR' : os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/cab',

        'BASE_PATH' : os.path.dirname(os.path.dirname(os.path.abspath(__file__))),

        # SECURITY WARNING: keep the secret key used in production secret!
        'SECRET_KEY' : '+v6y=)a(@e_7be-*=mcvnqd7^-0ey@&cdh1$r64+%i0o+swv(k' ,

        # SECURITY WARNING: don't run with debug turned on in production!
        'DEBUG' : True ,

        'ALLOWED_HOSTS' : [] ,
        
        # credential for connecting to database
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'cab',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : 3306,


        'server_http' : 'https://'
        
        }

    return credentials