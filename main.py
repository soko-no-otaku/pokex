from flask import redirect, render_template
from urllib.parse import unquote
import functions_framework

@functions_framework.http
def ogp_proxy(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    POCKET_USER_AGENT = "PocketParser"

    request_args = request.args
    user_agent = request.user_agent.string

    if request_args and "url" in request_args:
        url = unquote(request_args["url"])

    if POCKET_USER_AGENT in user_agent:
        if request_args and "note" in request_args:
            note = unquote(request_args["note"])
            return render_template("ogp.html", note=note)
    else:
        return redirect(url)
