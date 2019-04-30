from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")  # Revisit decorators if you unclear of this syntax
def index():
    signed_in = False
    return render_template('index.html', signed_in=signed_in)


# @app.route('/user/<username>')
# def show(username):
#     return f"Hi {username[2]}"


if __name__ == '__main__':  # Revisit previous challenge if you're uncertain what this does https://school.nextacademy.com/courses/full-stack-web-development-bootcamp-with-python/lessons/2947
    app.run(debug=True)
