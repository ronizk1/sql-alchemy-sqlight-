31/12 class flask with sql - recipes
This line specifies the URI for connecting to the SQLite database:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
In this case, the database file is named recipes.db. (opened alone when running py app.py)
