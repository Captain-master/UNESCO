#全局数据
from flask import Flask
app = Flask(__name__)
import config

app.config.from_object(config)