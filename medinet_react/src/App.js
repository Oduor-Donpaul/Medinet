import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import MyNavbar from './components/Navbar';
import Home from './components/Home';
import Services from './components/Services';
import About from './components/About';

function App() {
  return (
    <BrowserRouter>
      <div className='App'>
        <MyNavbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/services' element={< Services />} />
          <Route path='/about' element={< About />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
