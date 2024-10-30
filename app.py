from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests

# Load env variables from .env file
load_dotenv()

app = Flask(__name__) # Class from flask module, represents web app

API_KEY=os.getenv('API_KEY')

@app.route('/')
def home():
    return render_template('index.html')
# @app.route('/weather', methods=['GET'])
# def get_weather():
#     city = request.args.get('city')
#     if not city:
#         return jsonify({'error': 'City parameter is missing'}), 400

#     # URL do zapytania do API OpenWeatherMap
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pl"

#     # Wysłanie zapytania do API
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         weather_data = {
#             'city': data['name'],
#             'temperature': data['main']['temp'],
#             'description': data['weather'][0]['description']
#         }
#         return jsonify(weather_data)
#     else:
#         return jsonify({'error': 'City not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/weather', methods=['GET'])
def getWeather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    # URL do zapytania do API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pl"

    # Wysłanie zapytania do API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        print("Weather Data Backend:", weather_data)
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)