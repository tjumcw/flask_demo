from model.user import User
from database import db


class UserDao:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, password):
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
