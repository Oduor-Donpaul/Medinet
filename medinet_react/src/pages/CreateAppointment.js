import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";

const CreateAppointment = () => {

    const [formData, setFormData] = useState({
        title: "",
        date: "",
        time: ""
    })

    const handleInputChange = (e) => {
        const {name, value} = e.target;
        setFormData({...formData, [name]: value})
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        console.log("data submitted", formData);

        setFormData({
            title: "",
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
                    <Form.Group controlId="title" >
                        <Form.Label>Title</Form.Label>
                        <Form.Control
                            type="text"
                            name="title"
                            value={formData.title}
                            onChange={handleInputChange}
                            
                            />

                    </Form.Group>

                    <Form.Group controlId="startDate">
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

export default CreateAppointment