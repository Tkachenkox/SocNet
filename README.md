Example of .env file:
```
SECRET_KEY="SecretKey"
SQLALCHEMY_TRACK_MODIFICATIONS=False
DB_DRIVER="postgresql_or_another"
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_HOST=host
POSTGRES_DB=db_name
PERSONS_PER_PAGE=5
```
  
To create migrations and run application correctly, need to run `export FLASK_APP=main:app` on Unix 
or `set FLASK_APP=main:app` on Windows 
Here slug is the name of commit.  
`flask db migrate -m "First migration"`  
Creating file with name `date_and_time_of_migration_first_migration`  
For insert fake data to database run `python insertion.py up`. This command insert fake data into tables.  
For clean database using `python insertion.py down`  
