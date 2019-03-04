import os

from flask import Flask


def create_app(test_config=None):
    # app creation and configuration
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
            )

    if test_config is None:
        # load the instance config, if exist while not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure the instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple about page
    @app.route('/about')
    def about():
        return 'In development'

    return app
