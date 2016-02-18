import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    host = os.environ['HOST'] if os.environ['HOST'] else '127.0.0.1'
    app.run(host=host)
