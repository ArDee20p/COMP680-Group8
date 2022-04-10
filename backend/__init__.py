import flask_login
import pymongo
from flask import Flask
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.secret_key = 'a0bgF^P(m*jy^iQ$jntTCxLp)raqqpAG'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

client = pymongo.MongoClient(
    "mongodb+srv://jlord:M0ng0DB@cluster0.lcjq9.mongodb.net/UserInfo?retryWrites=true&w=majority",
    server_api=ServerApi('1'))
db = client.get_database('LoginInfo')
coll = db.UserData

from backend import routes