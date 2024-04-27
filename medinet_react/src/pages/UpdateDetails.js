import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Form } from "react-bootstrap";

const UpdateDetails = () => {

    const [formData, setFormData ] = useState({
        firstName: '',
        lastName: '',
        phoneNumber: '',
        dateOfBirth: ''
    });

    //handle form input change
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name] : value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefaul();
    };

    return (
        <div>
            <div style={{marginTop: '10px', marginBottom: '10px' }} >
                <h2><b>Update Details</b></h2>
            </div>
            <div>
                <Form onSubmit={handleSubmit}>
                    <Form.Group controlId='firstName'>
                        <Form.Label>First Name</Form.Label>
                        <Form.Control
                        type="text"
                        name="firstName"
                        value={formData.firstName}
                        onChange={handleChange}
                        />
                    </Form.Group>

                    <Form.Group controlId="lastName">
                        <Form.Label>Last Name</Form.Label>
                        <Form.Control
                            type="text"
                            name="lastName"
                            value={formData.lastName}
                            onChange={handleChange}
                            required
                        />
                    </Form.Group>

                    <Form.Group controlId="dateOfBirth">
                        <Form.Label>Date of Birth</Form.Label>
                        <Form.Control
                            type="date"
                            name="dateOfBirth"
                            value={formData.dateOfBirth}
                            onChange={handleChange}
                            required
                        />
                    </Form.Group>

                    <Form.Group controlId="phoneNumber">
                        <Form.Label>Medical History</Form.Label>
                        <Form.Control
                            type="text"
                            name="phoneNumber"
                            value={formData.phoneNumber}
                        />
                    </Form.Group>


                </Form>

            </div>
        </div>
    )
}

export default UpdateDetails
