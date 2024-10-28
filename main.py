from flask import Flask

app = Flask(__name__) # Class from flask module, represents web app

@app.route('/') # Function that handles queries to the main page
def weather():
    return "Hello, World!"




if __name__ == '__main__':
    app.run()