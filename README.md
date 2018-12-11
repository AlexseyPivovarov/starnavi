
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
pip3 install -r requirements.txt
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
    >Receive request with Json like  
    ```json
    {
        "username": "some_name",
        "password": "some_password"
    }
    ```   
    >Will return http response status code 200 (OK) and Json with JWT, like  
    ```json
    {
        "access": "access_token",
        "refresh": "refresh_token"
    }
    ```
    >Or, if no active account found with the given credentials, will return http response status code 400 (Bad Request) and Json like
    ```json
    {
        "non_field_errors": [
            "No active account found with the given credentials"
        ]
    }
    ```
    
- POST /auth/login/refresh/       
    The endpoint that will refresh the token
    >Receive request with Json like
    ```json
    {
        "refresh": "refresh_token"
    }
    ```    
    >Will return http response status code 200 (OK) and Json with new access token, like 
    ```json
    {
        "access": "access_token"
    }
    ```
    >Or, if wrong access token went reseiver, will return http response status code 401 (Unauthorized) and Json like
    ```json
    {
        "detail": "Token is invalid or expired",
        "code": "token_not_valid"
    }
    ```

- POST /auth/register/    
    The endpoint that will register the new user
    >Receive request with Json like
    ```json
    {
        "username": "some_name",
        "password": "some_password"
    }
    ```    
    >Will return http response status code 201 (Created) and Json with created user info, like 
    ```json
    {
        "username": "some_name",
        "password": "some_password"
    }
    ```
    >Or, if no valid email went reseiver, will return http response status code 400 (Bad Request) and Json like
    ```json
    {
        "username": [
            "Enter a valid email address."
        ]
    }
    ```
    >Or, if A user with that email already exists, will return http response status code 400 (Bad Request) and Json like
    ```json
    {
        "username": [
            "A user with that username already exists."
        ]
    }
    ```
     >It is optionally possible to connect mail validation via clearbit.com by setting the value of the  
     CLEARBIT_CHECK = True, that constant in the module settings.py  
     If the email did not pass validation by clearbit.com, will return http response status code 500 (Internal Server Error) and Json like
    ```json
    {
        "Error": [
            "The given email is invalid"
        ]
    }
    ```
    
- POST /posts/add/    
    The endpoint that will create the new post, for registered users only
    >Receive request with {"title": "some_title", "body": "some_body"} as data    
    and {"Authorization": "Bearer access_token"} in headers   
    Will return a created post if successful or an error message if something went wrong, as Json   

- PATCH /posts/like/<title>/    
    The endpoint that will update the likes counter in the post, only for registered users
    ><title> - the title of the post you want to update    
  
    >Receive request with {"Authorization": "Bearer access_token"} in headers   
    Will return an updated post if successful or an error message if something went wrong, as Json   

- PATCH /posts/unlike/<title>/    
    The endpoint that will update the unlikes counter in the post, only for registered users
    ><title> - the title of the post you want to update    
  
    >Receive request with {"Authorization": "Bearer access_token"} in headers   
    Will return an updated post if successful or an error message if something went wrong, as Json   
