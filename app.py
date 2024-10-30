from flask import Flask, request, jsonify, render_template, redirect, url_for
from dotenv import load_dotenv
import os
import requests

# Load env variables from .env file
load_dotenv()

API_KEY=os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')

        return render_template('weather.html', city=city)
    
    else:
        #return "Proszę przesłać nazwę miasta przez formularz na stronie głównej.", 405
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)