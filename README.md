# MovieDB REST API

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Improvements](#improvements)

## General info
This project contains REST APIs for a Movie Database where 
* public users can use the service to search for movies by name, genre and be able to sort
and filter the results by votes, genre
* Registered/Authenticated users should be able to add movies, upvote/downVote
movies, set favourite genre and get recommendations based on favourite genre.
* Authentication is done using JWT.
	
## Technologies
Project is created with:
* Django==3.2
* djangorestframework==3.12.4
* djangorestframework-simplejwt==5.0.0
* mysqlclient==2.0.3
* PyJWT==2.3.0
	
## Setup
The first thing to do is to clone the repository:

```
$ git clone https://github.com/DivyaMChandrasekaran/MovieDB.git
$ cd MovieDBRestAPI
```

Create a virtual environment

```
$ python3 -m venv devenv
$ source devenv/bin/activate
```

Install dependencies 

```
$ pip3 install -r requirements.txt
```

Go to the project folder and run the project
```
$ cd MovieDBRestAPI
$ python manage.py runserver
```

Mysql Database configuration: 

Go to mysql prompt and create database  , user and grant privileges

```
1. create database movies;
2. CREATE USER 'movies_root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'movies@123';
3. GRANT ALL ON movies.* TO 'movies_root'@'localhost';
4. FLUSH PRIVILEGES;
```

In the django folder , run the below commands :
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Improvements
* Rate API Limit can be implemented to limit the API calls
