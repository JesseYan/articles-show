#!venv/bin/python

__author__ = 'jesse'


from flask_user import SQLAlchemyAdapter, UserManager

from app import myapp, db
from app.user_role_model import User, Role
from app import index_view


# def create_app(test_config=None):                   # For automated tests
#
#     # Reset all the database tables
#
#     db.create_all()
#
#     # Setup Flask-User
#     db_adapter = SQLAlchemyAdapter(db,  User)
#     user_manager = UserManager(db_adapter, myapp)
#
#     # Create 'user007' user with 'secret' and 'agent' roles
#     if not User.query.filter(User.username=='user007').first():
#         user1 = User(username='user007', email='user007@example.com', active=True, password=user_manager.hash_password('Password1'))
#         user1.roles.append(Role(name='secret'))
#         user1.roles.append(Role(name='agent'))
#         db.session.add(user1)
#         db.session.commit()
#
#     return myapp


from flask_user import roles_required, login_required
from flask import render_template_string, render_template
from app import myapp


# The Home page is accessible to anyone
@myapp.route('/')
def home_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>Home page</h2>
            <p>This page can be accessed by anyone.</p><br/>
            <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
            <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
            <p><a href={{ url_for('special_page') }}>Special page</a> (login with username 'user007' and password 'Password1')</p>
        {% endblock %}
        """)


# The Members page is only accessible to authenticated users
@myapp.route('/members')
@login_required                                 # Use of @login_required decorator
def members_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>Members page</h2>
            <p>This page can only be accessed by authenticated users.</p><br/>
            <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
            <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
            <p><a href={{ url_for('special_page') }}>Special page</a> (login with username 'user007' and password 'Password1')</p>
        {% endblock %}
        """)


# The Special page requires a user with 'special' and 'sauce' roles or with 'special' and 'agent' roles.
@myapp.route('/special')
@roles_required('secret', ['sauce', 'agent'])   # Use of @roles_required decorator
def special_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>Special Page</h2>
            <p>This page can only be accessed by user007.</p><br/>
            <p><a href={{ url_for('home_page') }}>Home page</a> (anyone)</p>
            <p><a href={{ url_for('members_page') }}>Members page</a> (login required)</p>
            <p><a href={{ url_for('special_page') }}>Special page</a> (login with username 'user007' and password 'Password1')</p>
        {% endblock %}
        """)


# Start development web server
if __name__ == '__main__':
    # article_app = create_app()
    # article_app.run(host='0.0.0.0', port=5000, debug=True)
    myapp.run(host='0.0.0.0', port=5000, debug=True)
