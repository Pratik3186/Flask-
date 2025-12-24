from flask import Flask, render_template

# It creates an instance of the flask class,
# which acts as the WSGI application.

app = Flask(__name__)

@app.route("/")
def welcome():
    """
    This function is decorated with @app.route("/"),
    which means it will be executed when the root URL ("/") is accessed.
    It returns a simple welcome message.
    """
    return "<html><H1>About This Application</H1><p>This Flask application demonstrates basic routing and view functions.</p></html>"


@app.route("/about")
def about():
    """
    This function is decorated with @app.route("/about"),
    which means it will be executed when the "/about" URL is accessed.
    It returns a brief description of the application.
    """
    return render_template("index.html")

if __name__ == "__main__":
    """
    The app.run() method runs the application on a local development server.
    The debug=True argument enables debug mode, which provides detailed error pages and auto-reloads the server on code changes.
    """
    port = 5000
    print(f"Starting Flask application on port {port}")
    print(f"Access the application at: http://localhost:{port}")
    app.run(debug=True, use_reloader=True, port=port)
