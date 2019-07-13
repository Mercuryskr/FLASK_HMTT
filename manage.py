from info import create_app, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
"""
从单一职责的原理来思考：manage.py文件只需要负责项目启动&数据库迁移即可，其他的配置信息，app相关信息都应该抽取到特定文件中。
"""

# 传入的参数是development获取开发模式对应的app对象
# 传入的参数是production获取线上模式对应的app对象
app = create_app('development')

# 6.创建管理对象
manager = Manager(app)

# 7.创建迁移对象
Migrate(app, db)

# 8.添加迁移命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # app.run()
    # 9.使用管理对象运行项目
    manager.run()
