from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dastanio2020@localhost/money'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tableone(db.Model):
    __tablename__ = 'tableone'
    id = db.Column(db.Integer, primary_key=True)
    coin_name = db.Column(  db.Unicode)
    latest_news = db.Column(db.Unicode)


    def __init__(self, coin_name, latest_news):
        self.coin_name = coin_name
        self.latest_news = latest_news