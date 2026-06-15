console.log("script.js connected");
function getWeatherCondition(code) {

            if (code === 0) {
                return {
                    icon: "☀️",
                    text: "Clear Sky"
                };
            }

            if ([1, 2, 3].includes(code)) {
                return {
                    icon: "☁️",
                    text: "Cloudy"
                };
            }

            if ([45, 48].includes(code)) {
                return {
                    icon: "🌫️",
                    text: "Fog"
                };
            }

            if ((code >= 51 && code <= 67) ||
                (code >= 80 && code <= 82)) {
                return {
                    icon: "🌧️",
                    text: "Rain"
                };
            }

            if (code >= 71 && code <= 77) {
                return {
                    icon: "❄️",
                    text: "Snow"
                };
            }

            if (code >= 95) {
                return {
                    icon: "⛈️",
                    text: "Thunderstorm"
                };
            }

            return {
                icon: "🌦️",
                text: `Weather Code ${code}`
            };
        }

        async function getWeather() {

            try { 

            let city = document.getElementById("city").value;

            if (city.trim() === "") {

                alert("Please enter a city name");

                return;
            }

            document.getElementById("result").innerHTML =
            `
            <div class="loader"></div>
            <p>Loading weather data...</p>
            `;

            let response = await fetch(
                `http://127.0.0.1:8000/weather?city=${city}`
            );

            let data = await response.json();

            let condition = getWeatherCondition(data.weather_code);
            let container = document.getElementById("container");
            container.className = "container";

            if (condition.text === "Clear Sky") {

                container.classList.add("sunny");

            }
            if (condition.text === "Cloudy") {

                container.classList.add("cloudy");

            }
            if (condition.text === "Rain") {

                container.classList.add("rainy");

            }
            if (condition.text === "Thunderstorm") {

                container.classList.add("storm");

            }
            if (condition.text === "Snow") {

                container.classList.add("snowy");

            }
            if (condition.text === "Fog") {

                container.classList.add("foggy");

            }

            document.getElementById("result").innerHTML =
            `
                <div class="weather-card">

                    <div class="weather-icon">
                        ${condition.icon}
                    </div>

                    <h2>${data.city}</h2>

                    <div class="temp">
                        ${data.temperature}
                    </div>

                    <p>💨 Wind Speed: ${data.wind_speed}</p>

                    <p>🌤️ ${condition.text}</p>

                </div>
            `;
                }

                catch(error) {

                    document.getElementById("result").innerHTML =
                    `
                    <p>❌ Something went wrong.</p>
                    `;

                    console.error(error);
    }
        }
        document
    .getElementById("city")
    .addEventListener("keypress", function(event) {

        if (event.key === "Enter") {

            getWeather();

        }
    });