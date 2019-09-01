from flask import Blueprint

web = Blueprint("web", __name__)

from app.web import book # 不导入不执行