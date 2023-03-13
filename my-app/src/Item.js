import React, { useContext } from "react";
import { ListContext } from "./Context";

const Item = ({ item, index }) => {
  const { removeItem } = useContext(ListContext);
  return (
    <div>
      <span>{item}</span>
      <button onClick={() => removeItem(index)}>X</button>
    </div>
  );
};

export default Item;
