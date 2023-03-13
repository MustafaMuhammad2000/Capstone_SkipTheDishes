import React, { useState, useContext } from "react";
import { ListContext } from "./Context";

import styles from "./App.css";
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

function ButtonCollapse({ cusine }) {
  const [open, setOpen] = useState(false);
  const { list, addItem } = useContext(ListContext);
  console.log(list);
  return (
    <div>
      <div className="d-grid gap-2">
        <Button
          onClick={() => setOpen(!open)}
          aria-controls="example-collapse-text"
          aria-expanded={open}
          variant="primary"
          size="lg"
        >
          {cusine[0]}
        </Button>
      </div>

      <Collapse in={open}>
        {/* <div id="example-collapse-text">
          Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
          terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer
          labore wes anderson cred nesciunt sapiente ea proident.
        </div> */}
        <div>
          {cusine.slice(1).map(function (item) {
            return (
              <Button
                variant="primary"
                className="custom-btn"
                key={item}
                onClick={() => addItem(item)}
              >
                {item}
              </Button>
            );
          })}
        </div>
      </Collapse>
    </div>
  );
}

export default ButtonCollapse;
