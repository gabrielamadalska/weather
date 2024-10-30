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

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pl"
        response = requests.get(url)
        print('response', response)
        data = response.json()
        
        #if response == 200
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        print(weather_data, 'data')



        return render_template('weather.html', weather_data=weather_data)
    
    else:
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True)