from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


app = Flask(__name__)
db_path = os.path.join(os.getcwd(), 'new-movies-collection.db')
print(f'Database will be created at: {db_path}')
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # disables tracking modifications
Bootstrap5(app)
db = SQLAlchemy(app)

# CREATE DB
# Defines the Book model (modern approach, with Type Checking)
class Movie(db.Model):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(Float, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(Float, nullable=False)
    img_url: Mapped[str] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


# CREATE TABLE



@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
