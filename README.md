# GNotes
An attempted clone of google keep 

## Installation

1. git clone project
```
git clone git@github.com:andela-ooshodi/gnotes.git
```

2. Create a database "gnotes" in your PostgreSQL DB (create your own DB if need be)
```
psql
create database gnotes;
\q
```

3. Run project
```
python manage.py runserver
```

4. Navigate to the project with your browser
```
http://localhost:8000/
```