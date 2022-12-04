import logging
from flask import Blueprint, jsonify
from utils import get_post_by_pk, get_posts_all

"""Логирование обращений к эндпоинтам API"""
_log_format = f"%(asctime)s [%(levelname)s] %(message)s"

def get_file_handler():
    file_handler = logging.FileHandler("logs/api.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))

    return file_handler

def get_logger():
    logger = logging.getLogger("logs/api.log")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())

    return logger

posts = get_posts_all()
logs = get_logger()

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/posts') #Представление, которое обрабатывает запрос GET /api/posts и возвращает полный список постов в виде JSON-списка

def get_all_posts_json():
    logs.info(f'api_posts - > {len(posts)}')
    return jsonify(posts)

@api_blueprint.route('/api/posts/<int:post_id>') #Представление, которое обрабатывает запрос GET /api/posts/<post_id> и возвращает один пост в виде JSON-словаря

def get_post_json(post_id):
    post = get_post_by_pk(post_id)
    logs.info(f'api_posts - > {post_id}')
    return jsonify(post)
