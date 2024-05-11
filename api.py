from flask import Flask, url_for, request
from markupsafe import escape
from controller import todos_controller


app = Flask(__name__)
app.register_blueprint(todos_controller.router, url_prefix='/todos')


@app.route('/')
def index():
    return '<div>Index Page</div>'


@app.route("/home", methods=['GET', 'POST'])
def home():
    return "<p>Hello, welcome home</p>"


@app.route("/profile/<string:user_id>")
def profile(user_id):
    return f"<p>Your id is {user_id}!</p>"


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('home'))
#     print(url_for('home', next='/'))
#     print(url_for('profile', user_id='John Doe'))


# if __name__ == '__main__':
#     app = create_app()
#     app.run(port="6000")
