import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from 'axios'

const CreateAppointmentForm = ({defaulPractitioner, defaultService}) => {

    const [formData, setFormData] = useState({
        patient: '',
        practitioner: defaulPractitioner || '',
        service: defaultService || '',
        date: "",
        time: "",
        status: 'pending'
    })

    const handleInputChange = (e) => {
        const {name, value} = e.target;
        setFormData({...formData, [name]: value})
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost/api/appointment/<int:pk>/');
            console.log("Appointment created:", response.data);
        } catch (error) {
            console.error('Error creating appointment:', error)
        }

        console.log("data submitted", formData);

        setFormData({
            date: "",
            time: ""
        })
    }

    return (
        <div style={{width: '100%'}}>
            <div>
                <h2><b>Create Appointment</b></h2>
            </div>
            <div style={{display: 'flex', justifyContent: 'center', width: '100%', alignItems: 'center'}}>
                <Form onSubmit={handleSubmit}>

                    <Form.Group controlId="patient">
                        <Form.Label>Patient</Form.Label>
                        <Form.Control
                            type="text"
                            name="patient"
                            value={formData.patient}
                            onChange={handleInputChange}
                        />
                    </Form.Group>

                    <Form.Group controlId="practitioner">
                        <Form.Label>Practitioner</Form.Label>
                        <Form.Control
                            type="text"
                            name="practitioner"
                            value={formData.practitioner}
                            onChange={handleInputChange}
                        />
                    </Form.Group>

                    <Form.Group controlId="service">
                        <Form.Label>Service</Form.Label>
                        <Form.Control
                            type="text"
                            name="service"
                            value={formData.service}
                            onChange={handleInputChange}
                        />
                    </Form.Group>

                    <Form.Group controlId="date">
                        <Form.Label>Date</Form.Label>
                        <Form.Control
                            type="date"
                            name="date"
                            value={formData.date}
                            onChange={handleInputChange}
                        />
                    </Form.Group>

                    <Form.Group controlId="time">
                        <Form.Label>Time</Form.Label>
                        <Form.Control
                            type="time"
                            name="time"
                            value={formData.time}
                            onChange={handleInputChange}
                        />



                    </Form.Group>

                    <Button variant="primary" type="submit" style={{marginTop: '15px'}} >
                        <small>Submit</small>
                    </Button>
                </Form>
            </div>
        </div>

    )
}

export default CreateAppointmentForm;