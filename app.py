from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    signed_in = True  # we are hardcoding this just to demonstrate how we can do conditionals in our template files
    return render_template('index.html', signed_in=signed_in)


@app.route("/contact")
def contact():
    signed_in = True  # we are hardcoding this just to demonstrate how we can do conditionals in our template files
    return render_template('contact.html', signed_in=signed_in)


if __name__ == '__main__':
    app.run()
