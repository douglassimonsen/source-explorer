from app import app
import flask


@app.route('/')
def main_route():
    return flask.render_template('index.html')