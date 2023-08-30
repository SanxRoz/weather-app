"use client";

import { useState } from "react";
import axios from "axios";

const WeatherForm = () => {
  const [cityName, setCityName] = useState("");
  const [weatherData, setWeatherData] = useState<any | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post("/api/weather", { cityName });
      setWeatherData(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          City Name:
          <input
            type="text"
            value={cityName}
            onChange={(e) => setCityName(e.target.value)}
          />
        </label>
        <button type="submit">Get Weather</button>
      </form>
      {weatherData && (
        <div>
          <h2>Weather Data</h2>
          <pre>{JSON.stringify(weatherData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default WeatherForm;
