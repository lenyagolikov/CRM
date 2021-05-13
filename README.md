# Basic CRM

1. Move to directory where the manage.py is located
2. Install requirements
<pre> <code> pip install -r requirements.txt </code> </pre>
3. Create database (in settings.py (folder - djcrm) congifure ONLY engine for DB)
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
</pre>
4. Create .env file using .template.env (in folder djcrm), fill in the fields (everything except mail), debug=True, any secret key, and database information. 
5. Use migrations
<pre> <code> python3 manage.py migrate </code> </pre>
6. Create superuser, if you need
<pre> <code> python3 manage.py createsuperuser </code> </pre>
7. Run server
<pre> <code> python3 manage.py runserver 5000 </code> </pre>
