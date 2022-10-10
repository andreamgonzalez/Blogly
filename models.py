"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

#BOILER PLATE CODE TO INCLUDE THE DATABSE IN FILE
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)

#MODELS GO BELOW
class User(db.Model):
    """User"""
    __tablename__ = 'users'

    # def __repr__(self):
    #     return f"<User id={self.id}"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text(50), nullable = False)
    last_name = db.Column(db.Text(50), nullable = False)
    image_url = db.Column(db.Text(500), nullable = False, default = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png')

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
