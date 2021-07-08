from flask import Flask
application = Flask(__name__)

counter = 0

@application.route("/")
def hello():
    counter += 1
    return "Hello World! " + int(counter)

if __name__ == "__main__":
    application.run()
