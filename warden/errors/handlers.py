from flask import Blueprint, render_template
import sys

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
# abort(404) will call this function
def page_not_found(error):
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
# abort(403) will call this function
def page_not_found_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
# abort(500) will call this function
def page_not_found_500(error):
    # get latest traceback info
    import traceback
    import sys
    traceback = traceback.print_exception(etype=sys.last_type,
        value=sys.last_value,
        tb=sys.last_traceback)
    return render_template('errors/500.html', error=error, traceback=traceback), 500
