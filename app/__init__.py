from flask import Flask 
from app.reports import ap
from app import users, reports
from app.users import user_print
app = Flask(__name__)
app.register_blueprint(ap)
app.register_blueprint(user_print)