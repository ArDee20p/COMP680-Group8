import sys
from flask import Flask, send_from_directory
from pywebio.platform.flask import webio_view
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.session import hold
from PIL import Image, ImageFilter
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
mstring = "mongodb+srv://bk7777:Csun%402022@cluster0.mwhha.mongodb.net/PROJECT"

client = MongoClient('mongodb+srv://bk7777:Csun%402022@cluster0.mwhha.mongodb.net/test?retryWrites=true&w=majority')
# client = MongoClient('mongodb+srv://%s:%s@cluster0.mwhha.mongodb.net' % ("bk7777", "Csun@2022"))
#client = MongoClient(mstring, 27017)
db = client.myFirstDatabase
emailCol = db["email"]
unameCol = db["username"]


# @app.route('/dbinput/', methods=['GET', 'POST'])
# def testdb():
#     credsToDB = {
#         'email': "john.smith@example.com",
#         'username': "jsmith1776",
#         'password': pbkdf2_sha256.hash("americathebeautiful")
#     }
#     db.insert_one(credsToDB)
#
# @app.route('/')
# def welcome():
#     popup("Welcome", [
#         put_text("Welcome to the application. Please register or login to continue."),
#         put_buttons(["Okay"], onclick=lambda _: close_popup())
#     ])
#
# def validateemail(p):
#     if emailCol.find({'email': p}):
#         return "This email already exists in our database."
#
# def validateusername(p):
#     if unameCol.find({'username': p}):
#         return "This username already exists in our database."
#
# @app.route('/register')
# def register(): #TODO: check for duplicate email & username
#     credentials = input_group("Registration Information", [
#         input("Email", name="email",
#               placeholder="Enter your email address",
#               required=True
#         ),
#         input("Username", name="username",
#               placeholder="Enter your desired username",
#               required=True
#               ),
#         input("Password", name="password",
#         type=PASSWORD,
#         placeholder="Enter your password",
#         help_text="Password should be at least 6 characters long.",
#         required=True
#         ),
#     ])
#  emailQuery =
#  if credentials.get("email") not in emailQuery:
#      credsToDB = {
#         'email': credentials.get("email"),
#         'username': credentials.get("username"),
#          'password': pbkdf2_sha256.hash(credentials.get("password"))
#      }
#      db.insert_one(credsToDB) #TODO: ensure that this is proper usage of insert_one()
# else:
#
#
#
#@app.route('/login')
#def login():
#
#    pbkdf2_sha256.verify("password", )