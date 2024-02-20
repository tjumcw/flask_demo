# app/controllers/user_controller.py
from flask import render_template, Blueprint, request
from service.user_service import UserService

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/')
def get_users():
    users = UserService.get_all_users()
    return render_template('users.html', users=users)


@user_blueprint.route('/register')
def register():
    return render_template("register.html")


@user_blueprint.route('/api/add', methods=['POST'])
def do_register():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    response = UserService.register_user(username, password)
    return response
