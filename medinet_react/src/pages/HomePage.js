import React from "react";
import { Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const HomePage = () => {

    return (
        <div>
            <div>
                {/* text input for searching doctors*/}
                <div className="d-flex justify-content-center" style={{paddingTop:'30px'}}>
                    <input name="doctor_search" 
                    type="text" 
                    placeholder="Search for doctors"
                    style={{width: '50%'}}
                    />
                </div>
            </div>
                <div style={{marginTop: '20px', marginLeft: '15px'}}>
                    <Card style={{width:'18rem'}} >
                        <Card.Img variant="top" alt="Image" />
                        <Card.Body>
                            <Card.Title>Title</Card.Title>
                            <Card.Text>
                                <p>Sample Text</p>
                                <p>experience</p>
                                <div className="d-flex justify-content-between align-items-cnter" >
                                    <small>avilability</small>
                                    <Button className="ms-right" >Book now</Button>
                                </div>
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </div>
            <div>

            </div>


        </div>
        
    )
}

export default HomePage;