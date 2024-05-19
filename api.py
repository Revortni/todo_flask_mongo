import traceback

from flask import Flask, url_for, request, jsonify
from markupsafe import escape

from resources import todos_rs


def create_app():
    app = Flask(__name__)
    API_URL_PREFIX = "/api/v1"
    app.register_blueprint(todos_rs.router, url_prefix=API_URL_PREFIX)

    @app.route('/')
    def index():
        return '<div>Index Page</div>'

    @app.route("/home", methods=['GET', 'POST'])
    def home():
        return "<p>Hello, welcome home</p>"

    @app.route("/profile/<string:user_id>")
    def profile(user_id):
        return f"<p>Your id is {user_id}!</p>"

    @app.errorhandler(Exception)
    def internal_server_error(exception):
        traceback.print_exception(
            type(exception), exception, exception.__traceback__)
        message = 'Internal Server Error'
        if hasattr(exception, 'message'):
            message = exception.message
        response = jsonify({'errors': [message]})
        response.status_code = 500
        return response

    return app

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('home'))
#     print(url_for('home', next='/'))
#     print(url_for('profile', user_id='John Doe'))


if __name__ == '__main__':
    app = create_app()
    app.run(port="6000", debug=True)
