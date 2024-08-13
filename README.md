# online-movie-ticket-booking-system
This is an online movie ticket booking website  made using following technologies:-
  1. Python-3.11
  2. Django-5.0.0
  3. JavaScript
  4. JQuery-3.3.1
  5. Bootstrap3

This project contains following apps:-
  1. theatre app
  2. movie app
  3. booking app
  4. home app
 
 In this project custom user model has been used rather than default user model.

 There are list and detail views of theatre, movie etc. 
 Movie list view displays the movie.
 Theatre list view displays all the theatres in a city.
 Booking list view displays our booking.


# How to run this project
Ensure you have docker installed on your system. If not, install it from [here](https://docs.docker.com/get-docker/)
on the Terminal or Command Prompt, run the following commands:-
1. run docker-compose up --build
2. open browser and go to 0.0.0.0:8000/
3. migrate the database using `docker-compose exec web python manage.py migrate`
4. create superuser using `docker-compose exec web python manage.py createsuperuser` and follow the instructions to create superuser
5. use the superuser credentials to login to the admin panel at 0.0.0.0:8000/admin or 0.0.0.0:8000/login
