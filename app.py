import logging

from flask import Flask, request, render_template, send_from_directory, jsonify
from utils import get_posts_all, get_all_comments, get_comments_by_post_id, get_posts_by_user, get_post_by_pk, search_for_posts
from api.api import api_blueprint

comments = get_all_comments()
posts = get_posts_all()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/') #Главная страница со всеми постами

def page_index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:postid>') #Страница определенного поста с комментариями

def show_post(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    count = len(comments)
    return render_template('post.html', post=post, comments=comments, count=count)

@app.route('/search') #Страница с результатами поиска по ключевому слову

def search_page():
    s = request.args['s']
    posts = search_for_posts(s)
    count = len(posts)
    return render_template('search.html', posts=posts, count=count)

@app.route('/users/<username>') #Страница определенного пользателя с его постами

def user_feed(username):
    user_posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, username=username)

@app.errorhandler(500)
def server_error(e):
    return 'Ошибка 500'

@app.errorhandler(404)
def server_error(e):
    return 'Ошибка 404'

"""Регистрация представлений, которые обрабатывают GET запросы"""
app.register_blueprint(api_blueprint)

app.run(debug=True)