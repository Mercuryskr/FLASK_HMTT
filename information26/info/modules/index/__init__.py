from flask import Blueprint

# 1.创立蓝图对象
index_bp = Blueprint('index', __name__)

# 2. 将views文件中的视图函数和模块关联
from .views import *