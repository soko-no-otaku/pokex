from flask import render_template

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

    if POCKET_USER_AGENT in user_agent:
        if request_args and "note" in request_args:
            note = request_args["note"]
            return render_template("ogp.html", note=note)
    else:
        return "TODO: Redirect to given url"
