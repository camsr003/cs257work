from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to My Example Webpage."
    message = message + " This text was produced by concatenating strings in Python!"
    return render_template("homepage.html", someText = message)
@app.route('/newpage')
def nextpage():
    message = "This is the next page."
    return render_template("nextpage.html", someText = message)
if __name__ == '__main__':
    my_port = 5124
    app.run(host='0.0.0.0', port = my_port) 
