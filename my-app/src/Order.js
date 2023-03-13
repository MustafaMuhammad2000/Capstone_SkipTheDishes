import React, { useContext } from "react";
import { ListContext } from "./Context";

const Order = ({ order }) => {
  return (
    <div>
      <p>Items: {order.items.join(", ")}</p>
      <p>Date: {order.date}</p>
    </div>
  );
};

export default Order;
