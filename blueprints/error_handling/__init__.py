from flask import Blueprint

blueprint = Blueprint('error_handler', __name__,url_prefix='')


@blueprint.errorhandler(404)
def data_not_found(error):
    return 'Not Found'  # could have used a standard template/json shape
