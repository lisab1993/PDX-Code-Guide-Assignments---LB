from flask import Flask, render_template, request
import string, random



def generate(password_length):
    possibilities = string.ascii_letters + string.digits + string.punctuation
    password = ''
    length = int(password_length)
    x = 0
    while x < length:
        password += random.choice(possibilities)
        x += 1
    return password 

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    password_output = ''
    if request.method == 'POST':
        password_length = request.form['password_length']
        password_output = generate(password_length)
    return render_template('index.html', password_output=password_output)

app.run()





# Simple version: the user just enters in the number of characters in the password

# Complex version: the user enters the number of uppercase letters, 
#                  lowercase letters, numbers, and special characters
