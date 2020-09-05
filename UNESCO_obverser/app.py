from exts import app
from flask_cors import CORS
from Blue.login import sign_in
from Blue.index import index
from Blue.china_detail import CN
from Blue.news import news


app.register_blueprint(sign_in, url_prefix='/sign_in')
app.register_blueprint(index, url_prefix='/index')
app.register_blueprint(CN, url_prefix='/cn')
app.register_blueprint(news, url_prefix='/news')

CORS(app, supports_credentials=True)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
