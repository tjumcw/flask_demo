# config.py
import secrets


DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/flask'
# 关闭数据库修改跟踪操作[提高性能]，可以设置为True，这样可以跟踪操作：
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 开启SQL语句打印
SQLALCHEMY_ECHO = True
# 开启数据库的自动提交功能[一般不使用]
SQLALCHEMY_COMMIT_ON_TEARDOWN = False
# 连接池大小，默认为5
SQLALCHEMY_POOL_SIZE = 5
# 连接池超时时间，默认为10
SQLALCHEMY_POOL_TIMEOUT = 10
# 多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL ， Flask-SQLALchemy 自动设定 这个值为 2 小时。
SECRET_KEY = secrets.token_hex(16)  # session加密密钥
