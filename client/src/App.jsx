import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

export default function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    const { data } = await axios.get("/time", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
    console.log(data);
    setCurrentTime(data.time);
  }

  return (
    <div className="App">
      <header className="App-header">
        ... no changes in this part ...
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}
