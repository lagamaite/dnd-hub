// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
    // useState for setting an array of characters
    const [characters, setCharacters] = useState([]);

    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the array of characters from the /stats_display endpoint
        fetch("/stats_display").then((res) =>
            res.json().then((data) => {
                // Setting the array of characters from the API
                setCharacters(data);
            })
        );
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Character Stats</h1>
                {/* Mapping through the array of characters */}
                {characters.map((character, index) => (
                    <div key={index}>
                        <p>Character name: {character.character}</p>
                        <p>Strength: {character.strength}</p>
                        <p>Dexterity: {character.dexterity}</p>
                        <p>Constitution: {character.constitution}</p>
                        <p>Intelligence: {character.intelligence}</p>
                        <p>Wisdom: {character.wisdom}</p>
                        <p>Charisma: {character.charisma}</p>
                        <hr />
                    </div>
                ))}
            </header>
        </div>
    );
}

export default App;
