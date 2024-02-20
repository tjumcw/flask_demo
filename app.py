from flask import Flask
from controller.user_controller import user_blueprint
from database import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
# 数据库初始化
db.init_app(app)
app.register_blueprint(user_blueprint, url_prefix='/users')

# 创建所有数据库表
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
