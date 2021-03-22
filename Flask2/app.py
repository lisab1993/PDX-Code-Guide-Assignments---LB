from flask import Flask, render_template, request
import string, random



def generate_upper(uppercase):
    possibilities = string.ascii_uppercase
    uppercase_letters = ''
    upper = int(uppercase)
    x = 0
    while x < upper:
        uppercase += random.choice(possibilities)
        x += 1
        return uppercase_letters

 def generate_upper(uppercase):
    possibilities = string.ascii_uppercase
    uppercase_letters = ''
    upper = int(uppercase)
    x = 0
    while x < upper:
        uppercase += random.choice(possibilities)
        x += 1
        return uppercase_letters   




app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    password_output = ''
    if request.method == 'POST':
        uppercase = request.form['uppercase']
        lowercase = request.form['lowercase']
        special = request.form['special']
        password_output = generate(uppercase, lowercase, special)
    return render_template('index.html', password_output=password_output)

app.run()





# Simple version: the user just enters in the number of characters in the password

# Complex version: the user enters the number of uppercase letters, 
#                  lowercase letters, numbers, and special characters
