import logo from "./logo.svg";
import "./App.css";
import ButtonCollapse from "./ButtonCollapse";
import CForm from "./CForm";
import Results from "./Results";
import Submit from "./Submit";
import ClearButton from "./ClearButton";
import React, { useState } from "react";
import {
  Container,
  Button,
  Collapse,
  Alert,
  Table,
  Row,
  Col,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import ListContextProvider from "./Context.js";

function App() {
  return (
    <div className="App">
      <ListContextProvider>
        <CForm />
        <ClearButton />
        <Submit />
      </ListContextProvider>
    </div>
  );
}

export default App;
