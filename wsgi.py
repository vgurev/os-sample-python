from flask import Flask
application = Flask(__name__)

counter = 0

@application.route("/")
def hello():
    global counter
    counter += 1
    return "Hello World! " + str(counter)

if __name__ == "__main__":
    application.run()
