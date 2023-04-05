from flask import Flask

app = Flask(__name__)

@app.route('/')
def onepager():
    return

if __name__ == "__main__":
    app.debug = True
    app.run()