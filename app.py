# save this as app.py
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)