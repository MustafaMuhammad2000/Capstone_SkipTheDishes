import React, { useContext } from "react";
import { ListContext } from "./Context";
import Order from "./Order";

const ListOrders = () => {
  const { orders } = useContext(ListContext);
  console.log(orders);

  return (
    <div>
      <p>Past Orders:</p>
      {orders.map((order, index) => (
        <Order key={index} order={order} />
      ))}
    </div>
  );
};

export default ListOrders;
