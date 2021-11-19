Example of database.env file:
```
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_user_password
POSTGRES_DB=name_of_db
```

Example of .env file:
```
SECRET_KEY="SecretKey"
SQLALCHEMY_TRACK_MODIFICATIONS=False
DB_DRIVER="postgresql_or_another"
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_user_password
POSTGRES_HOST=host
POSTGRES_DB=name_of_db
PERSONS_PER_PAGE=5
LOGGER_FROMATTER=%(asctime)s:%(name)s:%(levelname)s:%(message)s
LOG_LEVEL=INFO
LOG_PATH=app.log
LEVEL_CONSTANT = 5
```

To create migrations and run application correctly, need to run `export FLASK_APP=main:app` on Unix 
or `set FLASK_APP=main:app` on Windows 
Here slug is the name of commit.  
`flask db migrate -m "First migration"`  
Creating file with name `date_and_time_of_migration_first_migration`  
For insert fake data to database run `python insertion.py up`. This command insert fake data into tables.  
For clean database using `python insertion.py down`  
