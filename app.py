
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    print("Hello Container... Apr 2 10:28 ########")
    return "Hello World 22 CodeBUild Apr 1 18:47!"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8080"), debug=True)