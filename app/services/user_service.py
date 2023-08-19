import app.repositories.user_repository as user_repository

def create_user(body):
    return user_repository.create_user(body)