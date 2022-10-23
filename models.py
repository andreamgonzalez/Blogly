"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
import datetime

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

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Blog post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # tags = db.relationship("PostTag", backref="Post")

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

class Tag(db.Model):
    """Tag to add on posts"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship("Post", secondary="posts_tags", backref="tags")


class PostTag(db.Model):
    """Tag on post."""

    __tablename__ = "posts_tags"

    # id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True, nullable=False)
