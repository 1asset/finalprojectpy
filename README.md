# Final Project - Advanced Programming in Python 
It's the final project of our group consist of 3 students (Asset Kanatov, Dias Karibaev, Yeskendir Iskakov)
We integrated Assignment 3 and Assignment 4 projects into one project and completed bootstrap design for the pages

# Installation
Before starting to use the code you must install required packages and modules. All packages and libraries will be provided in requirements.txt file, that is uploaded in the repository. Basically, you'll need the packages that are provided below:

``` 
flask (https://flask.palletsprojects.com/en/2.0.x/)
flask_sqlalchemy (https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
requests  (https://pypi.org/project/requests/)
beautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Huggingface(pip install transformers)
```

# Usage
At first we need to create a database in DBMS application(SQL server,Pgadmin) or other database management system. After that, you need to successfully connect your server with the database. We called our database "assignment4" as it is shown in the code. Also, it's important to know the login and password of your database, ours is postgres and 5432.
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/flask'
```
The next step is to create a table in your new database, the database name is assignment4.
```
CREATE TABLE Paragraphs (
id INTEGER PRIMARY KEY,
coin_name VARCHAR,
title VARCHAR,
body VARCHAR, 
link VARCHAR
)
```
Also, we are creating the Clients table:
```
CREATE TABLE Clients (
id INTEGER PRIMARY KEY,
login VARCHAR,
password VARCHAR,
token VARCHAR
```

Further step is to run main.py file, you'll get the IP-address in the terminal that you need to follow, after following it, you need to log in on the website. The link is below:
```
http://127.0.0.1:5000
```

Then, after logging in, you will be redirected to the coin page where you can search the exact token. Also, if you add /token to the path, you'll see your exact token that you can use to be verified on /protected path. When you follow /protected path, you enter your token and after than there will be a verification of your profile.

# Examples

### This is the home page of the website, you need to press log in
![1](https://user-images.githubusercontent.com/82859085/142574009-19ab01af-1c7f-40eb-b538-8fb8c189a596.PNG)

### Here you enter the login and password from the database, after that you're gonna be redirected to the coin page.
![2](https://user-images.githubusercontent.com/82859085/142574134-0f9e1bcc-e928-4270-87ea-a0d89a68afb2.PNG)

### It is the coin page, where you can search for the coins from coin market
![9](https://user-images.githubusercontent.com/82859085/142574178-e81e98b8-6336-46e9-acf5-114b7ff6a44e.PNG)

### Here are the examples of using tokens and being verified
![6](https://user-images.githubusercontent.com/82859085/142574267-26d2e73b-72ae-4be0-bae0-7890d9bde9fa.PNG)
![7](https://user-images.githubusercontent.com/82859085/142574545-f0519c63-453f-4e58-a81e-1863374e302f.PNG)
![8](https://user-images.githubusercontent.com/82859085/142574316-41362096-4a6c-4d72-8214-f05b27b3a1b8.PNG)

### And here is the usage of the database, 2 tables from the PostgreSQL

![3](https://user-images.githubusercontent.com/82859085/142574433-e9758a9b-70f9-44e5-a3d7-9e96b34093ab.PNG)
![4](https://user-images.githubusercontent.com/82859085/142574440-6cbfe515-508d-4d26-990f-1003c27feeb9.PNG)







