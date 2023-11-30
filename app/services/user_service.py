import app.repositories.user_repository as user_repository


def create_user(body):
    return user_repository.create_user(body)


def get_user_by_id(id):
    return user_repository.get_user_by_id(id)
