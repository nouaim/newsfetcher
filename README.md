# The goal of this project

Get data the first time from the [newsapi](https://newsapi.org) directly, and show it to the client. Then store it in a PostgreSQL database. 

If the client clicks get, give it the data from the database.
Within one hour update the database.

If the same request is made by the same client serve it from the cache.
	
# Steps to run the project

1. Create a virtual environment:
2. ```python3 -m venv venv```
4. ```source venv/bin/activate```
5. ```pip install -r requirements.txt```
6. Install Postgres (with docker or whatever suitable option for you)
7. Run postgres
```shell
$ sudo docker run --name postgresql2 -e POSTGRES_PASSWORD=1qar2esx@ -p 5432:5432 -d postgres  ## postgresql2 is the name of the database
```
8. Test the database (optional)
```shell
$ psql -h localhost -p 5432 -U postgres ## you will need to password (1qar2esx@ in our example)
$ \c postgres 
$ \dt ## view the available tables in the database
$ \d proxy_newsitem  ## view our app table


![table](https://github.com/nouaim/newsfetcher/assets/29921701/2b34f183-21af-4b87-8a0c-c005ebffffd5)
```

```shell
$ select title from proxy_newsitem; ## to view the titles
```

![titles](https://github.com/nouaim/newsfetcher/assets/29921701/a973d82a-9df2-4e4d-ae44-7c2a551c03d4)


9. Add the configuration of the database in your ```.env``` file (port, host, passwords, etc)
10. run the following commands to start running django :
```shell
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
11. start celery server
```shell
sudo apt-get install rabbitmq-server

sudo systemctl enable rabbitmq-server

sudo systemctl start rabbitmq-server

sudo systemctl start rabbitmq-server  ## if you see "active" it means we are good
```
12. inside the project folder, run:
```shell
celery worker --loglevel=info
```
13. 





### Debugging

In order to debug celery tasks in the proxy app, run :

```shell
$ python manage.py shell
>>> from proxy.tasks import add  ## add is a function to add two numbers
>>> add.delay(5,6)
>>> add.apply_async((5,6) , countdown= 30)  ## delay 30 seconds
```
