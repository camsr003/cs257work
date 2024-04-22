import flask

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string
    
@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    addition = str(num1 + num2)
    return addition
    
@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Orange">' + word1 + '</h1>'

if __name__ == '__main__':
    my_port = 5124
    app.run(host='0.0.0.0', port = my_port) 