__author__ = 'jesse'

from flask_user import UserMixin
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from sqlalchemy.sql import func

from app import db


class Article(db.Model, UserMixin):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, server_default='')
    content = db.Column(db.Text, nullable=False, server_default='')
    author = db.Column(db.String(20), nullable=False, server_default='')
    create_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    update_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # update_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

    def __repr__(self):
        return '<Article %r>' % self.title


# Define the User profile form
class ArticleForm(Form):
    author = StringField('Article author', validators=[
        validators.DataRequired('Article author is required')])
    title = StringField('Article title', validators=[
        validators.DataRequired('Article title is required')])
    content = StringField('Article content', validators=[
        validators.DataRequired('Article content is required')])
    submit = SubmitField('Save')

