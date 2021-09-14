from flask import Flask, request, render_template

from views import product_app, service_app
import logging
from pythonjsonlogger import jsonlogger

app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")
app.register_blueprint(service_app, url_prefix="/services")
# logger = logging.getLogger()
# logHandler = logging.FileHandler('srv.log')
# logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)
handler = logging.FileHandler("test5.txt")
handler.setFormatter(formatter)# Create the file logger
app.logger.addHandler(handler)             # Add it to the built-in logger
# app.logger.setLevel(logging.DEBUG)

@app.route("/", methods=["GET", "POST"])
def index():
    app.logger.info('dfdfdfdfddfdf')
    return render_template("index.html")


# app.add_url_rule("/", "index", index)
# app.add_url_rule("/", view_func=index)

@app.route("/hello/")
@app.route("/hello/<string:name>/")
def hello(name=None):
    app.logger.info('dfdfdfdfddfdf')
    if name is None:
        name = "World"
    return f"<h1>Hello {name}!</h1>"


@app.route('/post/<string:post_id>/')
def alternative_show_post(post_id):
    # post_id > 0
    return 'Post (str) %r' % post_id


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post int %d' % post_id