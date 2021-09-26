# user_assignment
User CRUD operations with Django REST Framework
#### Note - Only Logged in user can able to perform CREATE, DETAIL, UPDATE, DELETE operation
## Instructions

### Start app from DockerFile
* docker-compose up

### Different operations
* Create super user: python manage.py createsuperuser
* [Login](http://0.0.0.0:8000) using created super user
* Display of all [Users](http:0.0.0.0:8000/user-list)
* Get User Detail :  http:0.0.0.0:8000/user-detail/{id}
* To add new user [Add User](http:0.0.0.0:8000/user-create)
* Update ONLY your details : http:0.0.0.0:8000/user-update/{id}
* Delete ONLY your account : http:0.0.0.0:8000/user-delete/{id}


### To run test cases
* python manage.py test app 
