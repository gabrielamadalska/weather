console.log("JavaScript file loaded");
async function getWeather() {
    console.log("1. getWeather function called"); // Dodaj tę linię
    const city = document.getElementById('city').value;
    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    try {
        const response = await fetch(`http://localhost:5000/weather?city=${city}`);
        console.log("Response Status:", response.status);
        const data = await response.json();
        console.log("Data received:", data);
        const weatherDiv = document.getElementById('weather-result');
        
        if (response.ok) {
            weatherDiv.innerHTML = `
                <h2>Weather in ${data.city}</h2>
                <p>Temperature: ${data.temperature}°C</p>
                <p>Describe: ${data.description}</p>
            `;
        } else {
            weatherDiv.innerHTML = `<p>${data.error}</p>`;
        }
    } catch (error) {
        console.error("Error:", error);
    }
}
