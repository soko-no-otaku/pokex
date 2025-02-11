from flask import redirect, render_template
from urllib.parse import unquote
import functions_framework
import re


@functions_framework.http
def pokex(request):
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

    if not "url" in request_args:
        raise RuntimeError("URL is required.")

    url = unquote(request_args["url"])
    is_x_url = re.search(
        r"https://x\.com/(?P<username>[0-9a-zA-Z]+)/status/[0-9]+", url
    )

    if POCKET_USER_AGENT in user_agent and is_x_url:
        return render_template("ogp.html", username=is_x_url.group("username"))
    else:
        return redirect(url)
