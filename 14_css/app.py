from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request
from flask import url_for

app = Flask(__name__)

@app.route("/")
def disp_loginpage():
    url_for('static', filename='style.css')

    return render_template( 'index.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()