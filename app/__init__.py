from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    #initialize application
    app = Flask (__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #intializing Flask extensions
    bootstrap.init_app(app)

    #Register Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting configuration
    from .requests import configure_request
    configure_request(app)

    return app
