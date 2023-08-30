"use client";

import { useState } from "react";
import axios from "axios";
import GetTime from "./components/GetTime";
import { capitalizeWords } from "../utils/stringHelpers";

const WeatherForm = () => {
  const [cityName, setCityName] = useState("");
  const [weatherData, setWeatherData] = useState<any | null>(null);

  const [unit, setUnit] = useState<string>("C");

  const toggleUnit = () => {
    setUnit((prevUnit) => (prevUnit === "C" ? "F" : "C"));
  };

  const displayTemperature = (): number => {
    const temp =
      unit === "C"
        ? weatherData.main.temp
        : weatherData.main.temp * (9 / 5) + 32;
    return Math.round(temp);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post("/api/weather", { cityName });
      setWeatherData(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const daysOfWeek = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  const currentDate = new Date();
  const currentDayIndex = currentDate.getDay();
  const currentDayName = daysOfWeek[currentDayIndex];

  return (
    <div className="body_div">
      <div className="input_div">
        <form onSubmit={handleSubmit}>
          <input
            className="input"
            type="text"
            value={cityName}
            onChange={(e) => setCityName(e.target.value)}
            placeholder="Search Here"
          />
          <button className="submit_button" type="submit">
            Get Weather
          </button>
        </form>
        <div className="switch">
          <input
            type="checkbox"
            id="unitToggle"
            onChange={toggleUnit}
            checked={unit === "F"}
          />
          <label htmlFor="unitToggle"></label>
        </div>
      </div>
      {weatherData && (
        <div className="weather_div">
          <div className="weather_data">
            <p className="bold_text">
              {weatherData.name}{" "}
              <span className="weather_number">
                {displayTemperature()}°{unit}
              </span>
            </p>

            <p>
              wind speed:{" "}
              <span style={{ fontWeight: "light" }}>
                {Math.round(weatherData.wind.speed * 3.6)} Km
              </span>
            </p>

            <GetTime />
            <p className="description">
              {capitalizeWords(weatherData.weather[0].description)}
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

export default WeatherForm;
