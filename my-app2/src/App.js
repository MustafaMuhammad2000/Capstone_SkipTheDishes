import logo from './logo.svg';
import './App.css';
import { Container,Button,Collapse,Alert,Table,counter } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from "react";

function App() {
  let [count, setCount] = useState(0);

  function incrementCount() {
    count = count + 1;
    setCount(count);
  }
  function decrementCount() {
    count = count - 1;
    setCount(count);
  }
  return (
    <div className="App">
      <div>{count}</div>
      <button onClick={incrementCount}>+</button>
      <button onClick={decrementCount}>-</button>
    </div>
  );
}

export default App;
