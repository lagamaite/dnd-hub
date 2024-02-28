// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from 'react-router-dom';
import "./App.css";
import StatComponent from "./components/StatComponent"
import Maps from "./components/Maps"
import Blog from "./components/blog/Blog"
import NavBar from "./components/NavigationBar"
import Home from "./components/Home"

function App() {
    // useState for setting an array of characters
    
return(
    <Router>
        <NavBar/>
      <Routes>
      <Route index element={<Home/>} />
      <Route path="maps" element={<Maps />} />
        <Route path="stats" element={<StatComponent />}>
        </Route>
      </Routes>
    </Router>
  );

}

export default App;

