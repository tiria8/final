import json

def get_posts_all():
    """
    возвращает посты
    :return: список всех постов пользователей
    """
    with open('C:\\Users\\daren\PycharmProjects\\final3\\data\\posts.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def get_all_comments():
    """
    Возращает все комментарии к постам
    :return: список комментариев к постам
    """
    with open('C:\\Users\\daren\\PycharmProjects\\final3\\data\\comments.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

comments = get_all_comments()
posts = get_posts_all()

def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя
    :param user_name: имя пользователя
    :return: список постов пользователя
    """
    user_posts = []
    for user in posts:
        try:
            if user_name.lower() == user['poster_name'].lower():
                user_posts.append(user)
        except ValueError:
            return 'Пользователь не найден'
    return user_posts

def get_comments_by_post_id(post_id):
    """
    возвращает комментарии определенного поста
    :param post_id: id поста
    :return: список комментариев поста
    """
    post_comments = []

    for comment in comments:
        try:
            if post_id == comment['post_id']:
                post_comments.append(comment)
        except ValueError:
            return 'Комментарии не найдены'
    return post_comments

def search_for_posts(query):
    """
    возвращает список постов по ключевому слову
    :param query: ключевое слово
    :return: список постов, содержащих ключевое слово
    """
    found_posts = []

    for post in posts:
        try:
            if query.lower() in post['content'].lower():
                found_posts.append(post)
        except ValueError:
            return 'Посты не найдены'
    return found_posts

def get_post_by_pk(pk):
    """
    возвращает один пост по его идентификатору
    :param pk: идентификатор поста
    :return: пост по идентификатору
    """
    for post in posts:
        if pk == post['pk']:
            user_post = post
    return user_post

