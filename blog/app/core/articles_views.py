__author__ = 'jesse'


from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_user import login_required, current_user

from app import app, db
from app.core.articles_models import ArticleForm, Article
from app.core.models import UserProfileForm


core_blueprint = Blueprint('core_articles', __name__, url_prefix='/articles/')


@core_blueprint.route('', methods=['GET'])
def articles_list_page():
    form = ArticleForm(request.form, current_user)

    articles = Article.query.all()
    # print articles
    # Process GET or invalid POST
    return render_template('articles/list_page.html', articles=articles)


@core_blueprint.route('create/', methods=['GET'])
@login_required
def articles_create_page():
    form = ArticleForm(request.form, current_user)
    return render_template('articles/create_page.html', form=form)


@core_blueprint.route('create/', methods=['POST'])
@login_required
def articles_upcreate_form():
    data = request.form
    article = Article(title=data.get('title'), author=current_user.first_name, content=data.get('content'))
    db.session.add(article)
    db.session.commit()
    return redirect('/articles/', code=302, )


# create or update an article: need login
@core_blueprint.route('edit/<article_id>/', methods=['GET', 'POST'])
@login_required
def articles_edit_form(article_id):
    aritcle = Article.query.filter_by(id=article_id).first()
    if request.method == "GET" and aritcle is not None and aritcle.author == current_user.first_name:
        # copy data to the form
        form = ArticleForm(request.form, aritcle)
        return render_template('articles/update_page.html', form=form, aritcle=aritcle)

    if request.method == "POST" and aritcle is not None and aritcle.author == current_user.first_name:

        data = request.form
        aritcle.title = data.get('title')
        aritcle.content = data.get('content')
        db.session.merge(aritcle)
        db.session.commit()
        get_flashed_messages("update success")
    return redirect('/articles/', code=302, )


# create or update an article: need login
@core_blueprint.route('delete/<article_id>/', methods=['GET', 'POST'])
@login_required
def articles_delete_form(article_id):
    aritcle = Article.query.filter_by(id=article_id).first()
    print "aritcle:", aritcle
    if request.method == "GET" and aritcle is not None and aritcle.author == current_user.first_name:
        # copy data to the form
        form = ArticleForm(request.form, aritcle)
        db.session.delete(aritcle)
        db.session.commit()
        # return render_template('articles/update_page.html', form=form, aritcle=aritcle)
        return redirect(url_for('core_articles.articles_own_page'), code=302, )
    return redirect(url_for('core_articles.articles_own_page'), code=302, )


@core_blueprint.route('own/', methods=['GET'])
@login_required
def articles_own_page():
    form = ArticleForm(request.form, current_user)
    my_name = current_user.first_name
    print 'my_name:', my_name
    article_list = Article.query.filter_by(author=my_name).all()

    return render_template('articles/own_page.html', form=form, articles=article_list)


# Register blueprint
app.register_blueprint(core_blueprint)
