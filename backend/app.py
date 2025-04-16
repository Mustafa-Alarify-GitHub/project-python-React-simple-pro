from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Routes
import routes

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

#  set FLASK_APP=app.py
# set FLASK_ENV = development
# flask run --reload
