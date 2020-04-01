
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    print("Hello Container...")
    return "Hello World 22 CodeBUild Mar 30 17:23!"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8080"), debug=True)