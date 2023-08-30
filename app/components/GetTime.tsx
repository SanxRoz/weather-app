import { useState, useEffect } from "react";

const GetTime = () => {
  const [currentDayName, setCurrentDayName] = useState("");
  const [currentTime, setCurrentTime] = useState("");

  useEffect(() => {
    const daysOfWeek = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];

    const updateDateTime = () => {
      const currentDate = new Date();
      const currentDayIndex = currentDate.getDay();
      const currentHour = currentDate.getHours();
      const currentMinutes = currentDate.getMinutes();
      const currentSeconds = currentDate.getSeconds();

      setCurrentDayName(daysOfWeek[currentDayIndex]);
      setCurrentTime(`${currentHour}:${currentMinutes}`);
    };

    const interval = setInterval(updateDateTime, 1000); // Update every second
    updateDateTime(); // Initial update
    return () => clearInterval(interval); // Cleanup on unmount
  }, []);

  return (
    <div>
      <p>
        {currentDayName}: {""}{" "}
        <span style={{ fontWeight: "light" }}>{currentTime}</span>
      </p>
    </div>
  );
};

export default GetTime;
