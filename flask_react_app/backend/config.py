from flask import Flask
from flask _sqlalchemy import SQLAlchemy
from flask_cors import  CORS


app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # not track all the modifications of the database

db = SQLAlchemy(app) # cratean instance of the database

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/mydatabase"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # not track all the modifications of the database
# db = SQLAlchemy(app) # cratean instance of the database
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/mydatabase"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # not track all the modifications of the database
# db = SQLAlchemy(app) # cratean instance of the database
 







