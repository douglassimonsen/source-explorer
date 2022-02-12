import flask
from app import app
import utils
import pathlib
redshift_dependencies_query = open(pathlib.Path(__file__).parent.joinpath('view_dependencies.sql')).read()
redshift_tables_query = open(pathlib.Path(__file__).parent.joinpath('tables_and_views.sql')).read()


@app.route('/api/views/redshift')
def get_views_redshift():
    with utils.get_conn() as conn:
        dependent_views = conn.to_json(redshift_dependencies_query)
        tables = conn.to_json(redshift_tables_query)
    return flask.jsonify({
        'dependencies': dependent_views,
        'objects': tables,
    })