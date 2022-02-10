from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

import config       

app = Flask(__name__,instance_relative_config=True)                 
app.config.from_pyfile('config.py')                                 
app.config.from_object(config.LiveConfig)                     

api = Api(app, doc="/swaggerdocs/")
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#load the routes
from projectapp.routes import user_routes,hn_routes,api_routes
from projectapp import mymodels