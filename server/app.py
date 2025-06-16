
import os
from flask import Flask, request, current_app, g, make_response, redirect, abort

app = Flask(__name__)

# --------------------
# Before Request Hook
# --------------------
@app.before_request
def set_app_path():
    # Store the absolute path of the application directory in g
    g.path = os.path.abspath(os.getcwd())

# --------------------
# Index Route
# --------------------
@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    path = g.path

    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {path}</h3>
    '''

    status_code = 200
    headers = {"Content-Type": "text/html"}

    return make_response(response_body, status_code, headers)

# --------------------
# Redirect Example
# --------------------
@app.route('/old')
def redirect_example():
    return redirect('/', 302)

# --------------------
# Abort Example
# --------------------
@app.route('/abort-example')
def abort_example():
    # Simulating a 404 error
    abort(404)

# --------------------
# Custom Count Route
# --------------------
@app.route('/count/<int:number>')
def count_to(number):
    count_list = [str(n) for n in range(number)]
    count_output = "\n".join(count_list) + "\n"  # Include final newline
    return make_response(count_output, 200, {"Content-Type": "text/plain"})

# --------------------
# Run the App
# --------------------
if __name__ == '__main__':
    app.run(port=5555, debug=True)
