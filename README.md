
**Requirements**    
Python 3.6, 3.7,
postgresql


**database preparation**
```
psql -U postgres
create user django_db_user with password 'django';
alter role django_db_user set client_encoding to 'utf8';
alter role django_db_user set timezone to 'Europe/Kiev';
alter user django_db_user createdb;
create database django_db owner django_db_user;
\q
```


**Install**
```
git clone https://github.com/AlexseyPivovarov/starnavi
cd starnavi/
pip install -r requarements.txt
python manage.py migrate
python manage.py createsuperuser
```


**Run application:**
```
python manage.py runserver :8080
```


**Usage:**

Available Endponits:

- POST /auth/login/   
    Login endpoint
    >Receive request with {'username': 'some_name', 'password': 'some_password'} as data    
    Will return Json with JWT, like {'access': 'access_token', 'refresh': 'refresh_token'}
    
- POST /auth/login/refresh/       
    The endpoint that will refresh the token
    >Receive request with {'refresh': 'refresh_token'} as data    
    Will return Json with new access token, like {'access': 'access_token'}

- POST /auth/register/    
    The endpoint that will register the new user
    >Receive request with {'username': 'user_mail', 'password': 'user_password'} as data     
    Will return a created user info if successful or an error message if something went wrong, as Json
    >>It is optionally possible to connect mail validation via clearbit.com  
    by setting the value of the CLEARBIT_CHECK = True, that constant in the module settings.py

- POST /posts/add/    
    The endpoint that will create the new post, for registered users only
    >Receive request with {'title': 'some_title', 'body': 'some_body'} as data    
    and {'Authorization': 'Bearer access_token'} in headers   
    Will return a created post if successful or an error message if something went wrong, as Json   

- PATCH /posts/like/<title>/    
    The endpoint that will update the likes counter in the post, only for registered users
    ><title> - the title of the post you want to update    
  
    >Receive request with {'Authorization': 'Bearer access_token'} in headers   
    Will return an updated post if successful or an error message if something went wrong, as Json   

- PATCH /posts/unlike/<title>/    
    The endpoint that will update the unlikes counter in the post, only for registered users
    ><title> - the title of the post you want to update    
  
    >Receive request with {'Authorization': 'Bearer access_token'} in headers   
    Will return an updated post if successful or an error message if something went wrong, as Json   
