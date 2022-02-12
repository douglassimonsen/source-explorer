import flask
from app import app
import utils
redshift_query = open(r'website\static\view_dependencies.sql').read()


@app.route('/api/views/redshift')
def get_views_redshift():
    with utils.get_conn() as conn:
        dependent_views = conn.to_json(redshift_query)
    return flask.jsonify(dependent_views)