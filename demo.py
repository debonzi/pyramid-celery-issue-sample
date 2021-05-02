from pyramid.config import Configurator


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        config.include("pyramid_celery")
        config.configure_celery(global_config["__file__"])

    return config.make_wsgi_app()
