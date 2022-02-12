import flask
from app import app
import utils
import pathlib
redshift_query = open(pathlib.Path(__file__).parent.joinpath('view_dependencies.sql')).read()


@app.route('/api/views/redshift')
def get_views_redshift():
    with utils.get_conn() as conn:
        dependent_views = conn.to_json(redshift_query)
    return flask.jsonify(dependent_views)