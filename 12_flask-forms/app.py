'''
Shinji, Jeffery, Sebastian
SoftDev
K<12> -- Post Get
<2022>-<17>-<10>
time spent: 2.60
'''


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) ## Print out the app name
    print("***DIAG: request obj ***")
    print(request) ## Prints out the request name/address
    print("***DIAG: request.args ***")
    print(request.args) ## Prints out the request information
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate(): ## Maybe more methods will work in the /auth root
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.form)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username']) This will work here, but not if uncommented in disp_loginpage
    print("***DIAG: request.headers ***")
    print(request.headers)
    print(request.method)
    return render_template( 'response.html', username = request.form['username'], requesttype=request.method )  #response to a form submission
'''
@app.route("/response", methods=['GET','POST'])
def response():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print(request.method)
    if request.method == 'POST':
    username=request.form['username']
    return (username)
return "aopa"
'''


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

