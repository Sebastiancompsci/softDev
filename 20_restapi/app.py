# Double S: Sebastian ching, Selena Ho
# SoftDev
# K20 -- NASA API Key
# 2022-11-22
# time spent: 0.5

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    f=open('key_nasa.txt', 'r') #accesses the file
    key=f.read() #key = content inside file (should be the api key from nasa)
    url=f"https://api.nasa.gov/planetary/apod?api_key={key}"
    content= requests.get(url).json()

    return render_template('main.html', image_url = content.get('url'), title = content.get('title'))

if __name__=="__main__":
    app.debug = True
    app.run()