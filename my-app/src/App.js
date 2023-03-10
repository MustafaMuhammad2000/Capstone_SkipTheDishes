import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
//import Button from 'react-bootstrap/Button';
// import Collapse from 'react-bootstrap/Collapse';
import { Container,Button,Collapse,Alert,Table } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {

  const [open, setOpen] = useState(false);

  return (
    <div className="App">
      <div className="d-grid gap-2">
        <Button 
          onClick={() => setOpen(!open)}
          aria-controls="example-collapse-text"
          aria-expanded={open}
          variant="primary" size="lg"
        >
          click
        </Button>
      </div>
      
      <Collapse in={open}>
        {/* <div id="example-collapse-text">
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
          terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer
          labore wes anderson cred nesciunt sapiente ea proident.
        </div> */}
        <Table>
          <tbody>
          <tr>
            <td><Button>Test1</Button></td>
            <td><Button>Test2</Button></td>
            <td><Button>Test3</Button></td>
          </tr>
          <tr>
            <td>Table cell</td>
            <td>Table cell</td>
            <td>Table cell</td>
          </tr>
          </tbody>
        </Table>
      </Collapse>

      <Collapse in={open}>
        {/* <div id="example-collapse-text">
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
          terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer
          labore wes anderson cred nesciunt sapiente ea proident.
        </div> */}
        <Table>
          <tbody>
          <tr>
            <td>Table cell</td>
            <td>Table cell</td>
            <td>Table cell</td>
          </tr>
          <tr>
            <td>Table cell</td>
            <td>Table cell</td>
            <td>Table cell</td>
          </tr>
          </tbody>
        </Table>
      </Collapse>
    </div>
  );
}

export default App;
