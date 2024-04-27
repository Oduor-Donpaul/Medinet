import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import MyNavbar from './components/Navbar';
import Services from './pages/Services';
import About from './components/About';
import HomePage from './pages/HomePage';
import DoctorDetails from './pages/DoctorDetails'
import UpdateDetails from './pages/UpdateDetails';
import ServiceDetails from './pages/ServiceDetails';
import CreateAppointment from './pages/CreateAppointment';

function App() {
  return (
    <BrowserRouter>
      <div className='App'>
        <MyNavbar />
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/practitioners/:id' element={<DoctorDetails /> } />
          <Route path='/services/:id' element={<ServiceDetails />} />
          <Route path='/services/:id/book' element={<CreateAppointment />} />
          <Route path='update-details' element={<UpdateDetails /> } />
          <Route path='/practitioner/:id/book' element={<CreateAppointment />} />
          <Route path='/services' element={< Services />} />
          <Route path='/about' element={< About />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
