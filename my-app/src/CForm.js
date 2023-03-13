import React, { useState, useContext } from "react";
import {
  Container,
  Button,
  Collapse,
  Alert,
  Table,
  Row,
  Col,
  Card,
  Form,
} from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import ButtonCollapse from "./ButtonCollapse";
import { ListContext } from "./Context";
import "./App.css";

function CForm() {
  const buttonStyle = { backgroundColor: "orange", border: "none" };
  const [open, setOpen] = useState(false);
  const { list, addItem } = useContext(ListContext);
  console.log(list);
  // const japanese = [
  //   "Japanese",
  //   "ramen",
  //   "sashimi",
  //   "teriyaki",
  //   "katsu",
  //   "tempura",
  //   "edamame",
  //   "bento",
  // ];
  // const mediterranean = [
  //   "Mediterranean",
  //   "pita",
  //   "damascus",
  //   "greek",
  //   "greece",
  //   "briam",
  //   "taramasalata",
  //   "opa",
  // ];
  // const indian = [
  //   "Indian",
  //   "naan",
  //   "samosa",
  //   "masala",
  //   "aloo",
  //   "paneer",
  //   "biryani",
  // ];
  // const italian = [
  //   "Italian",
  //   "pasta",
  //   "spaghetti",
  //   "penne",
  //   "fettuccini",
  //   "lasagna",
  //   "lasagne",
  //   "linguini",
  //   "ravioli",
  //   "tortellini",
  //   "meatball",
  //   "canoli",
  // ];
  // const chinese = ["Chinese", "hot pot", "wonton", "cantonese", "mein"];
  // const vietnamese = ["Vietnamese", "pho", "viet", "bun cha", "ca kho to"];
  // const mexican = [
  //   "Mexican",
  //   "chilaquiles",
  //   "burrito",
  //   "nacho",
  //   "quesadilla",
  //   "queso",
  // ];
  // const korean = [
  //   "Korean",
  //   "kimchi",
  //   "bulgogi",
  //   "bibimbap",
  //   "tteokbokki",
  //   "jjambbong",
  //   "doenjang",
  // ];
  // const thai = ["Thai", "tom yum goong", "green curry"];
  // const french = [
  //   "French",
  //   "foie gras",
  //   "coq au vin",
  //   "cassoulet",
  //   "baguette",
  //   "croissants",
  //   "gougeres",
  //   "cajun & creole",
  // ];
  // const african = [
  //   "African",
  //   "pap en vleis",
  //   "shisa nyama",
  //   "bunny chow",
  //   "koshari",
  // ];
  // const latinAmerican = [
  //   "Latin",
  //   "asado",
  //   "saltena",
  //   "feijoada",
  //   "empanada",
  //   "bandeja paisa",
  //   "gallo pinto",
  //   "ropa vieja",
  //   "mangu",
  //   "encebollado",
  //   "pupusas",
  //   "pepian",
  //   "peruvian",
  // ];
  // const ethiopian = ["Ethiopian", "tibs", "kitfo", "beyainatu", "fuul"];
  // const caribbean = ["Caribbean", "jamaica", "barbados", "bahamas"];
  // const filipino = ["Filipino", "adobo", "lechon", "sisig", "bulalo"];
  // const spanish = [
  //   "Spanish",
  //   "paella valenciana",
  //   "patatas bravas",
  //   "gazpacho",
  //   "pimientos de padron",
  //   "jamon",
  //   "tapas",
  // ];
  // const german = ["German", "schnitzel", "rouladen", "eintopf", "sauerbraten"];
  // const middleEastern = [
  //   "Middle Eastern",
  //   "falafel",
  //   "hummus",
  //   "shawarma",
  //   "baklava",
  //   "donair",
  // ];

  // const protein = ["Protein", "chicken", "fries", "beef", "pork"];

  const foodItems = [
    "Chinese Hotpot",
    "Vietnamese Beef Soup Noodles",
    "Thai Curry Chicken",
    "Korean Bulgogi (Beef BBQ)",
    "Indian Masala",
    "Pork Tonkotsu Ramen",
    "Mexican Burrito/Taco",
    "Foie Gras (French Goose Liver)",
    "Spaghetti/Pasta",
    "Poutine",
    "Sushi Roll",
    "Mediterranean",
    "Spanish",
    "Fried Chicken",
    "Butter Chicken",
    "Roasted Lamb",
    "Teriyaki Beef",
    "Beef Burger",
    "Steak",
    "Shrimp/Crab/Lobster",
    "Sausage",
    "Egg (Breakfast)",
    "Coffee/Tea",
    "Beer/Alcohol",
    "Ice Cream (Dessert)",
    "Barbecue",
    "Bubble Tea",
    "Fried Rice",
    "Fries",
    "Noodle Soup ",
    "Vegetable Salad",
    "Bakery (Cake/Donuts/Muffin/Cookie)",
  ];
  return (
    <div>
      <Row>
        {/* <Col>
          <Row>
            <ButtonCollapse cusine={japanese} />
          </Row>

          <Row>
            <ButtonCollapse cusine={mediterranean} />
          </Row>

          <Row>
            <ButtonCollapse cusine={indian} />
          </Row>

          <Row>
            <ButtonCollapse cusine={italian} />
          </Row>

          <Row>
            <ButtonCollapse cusine={chinese} />
          </Row>

          <Row>
            <ButtonCollapse cusine={vietnamese} />
          </Row>

          <Row>
            <ButtonCollapse cusine={mexican} />
          </Row>

          <Row>
            <ButtonCollapse cusine={korean} />
          </Row>

          <Row>
            <ButtonCollapse cusine={thai} />
          </Row>

          <Row>
            <ButtonCollapse cusine={french} />
          </Row>

          <Row>
            <ButtonCollapse cusine={african} />
          </Row>

          <Row>
            <ButtonCollapse cusine={latinAmerican} />
          </Row>

          <Row>
            <ButtonCollapse cusine={ethiopian} />
          </Row>

          <Row>
            <ButtonCollapse cusine={caribbean} />
          </Row>

          <Row>
            <ButtonCollapse cusine={filipino} />
          </Row>

          <Row>
            <ButtonCollapse cusine={spanish} />
          </Row>

          <Row>
            <ButtonCollapse cusine={german} />
          </Row>

          <Row>
            <ButtonCollapse cusine={middleEastern} />
          </Row>
        </Col> */}

        <Col>
          <Row>
            <div>
              {foodItems.map(function (item) {
                return (
                  <Button
                    variant="primary"
                    style={buttonStyle}
                    className="customed-btn"
                    key={item}
                    onClick={() => addItem(item)}
                  >
                    {item}
                  </Button>
                );
              })}
            </div>
          </Row>
        </Col>
      </Row>
    </div>
  );
}

export default CForm;
