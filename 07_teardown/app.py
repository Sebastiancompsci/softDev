#sdy: sebastian, david, yuki
# k07
# 2022-10-03
# time spent: 0.5 hr

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
- flask is java-like?
- running in terminal will give you a clickable link which will open a web server
in a browser
- general ip is the link to which is printed out in terminal
- no hablo queso is printed out in this window. our hypotheses in the following QCC was wrong,
but we had a pleasant surprise opening this.

QCC:
0. we have seen similar syntax in Java when creating objects from classes
1. / is a reference to the current directory or change of directory
2. this will print to the console. 
3. it will print a name of our choosing? or since we did not set __name__ to a string,
it will print None
4. this will appear in the terminal. we are guessing that since return is a function that
returns the value in terminal, it will appear there.
5. we have seen similar constructs in processing, which is a language that is based off java syntax.


...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 
 - We set about illuminating the cave of ignorance by sheer intuition and making inferences off
 past knowledge in courses like APCS.
'''
