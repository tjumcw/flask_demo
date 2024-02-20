from dao.user_dao import UserDao
from utils.result import build_error, build_success


class UserService:
    @staticmethod
    def get_all_users():
        return UserDao.get_all_users()

    @staticmethod
    def register_user(username, password):
        if not username or not password:
            return build_error("缺失必要参数")

        existing_user = UserDao.get_user_by_username(username)
        if existing_user:
            return build_error("用户名已存在")

        new_user = UserDao.create_user(username, password)
        return build_success("注册成功")
