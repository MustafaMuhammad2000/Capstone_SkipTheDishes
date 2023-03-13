import React, { useContext } from "react";
import { ListContext } from "./Context";
import Item from "./Item";

const Items = () => {
  const { list } = useContext(ListContext);
  console.log(list);

  return (
    <div>
      <p>Current list:</p>
      {list.map((item, index) => (
        <Item key={index} item={item} index={index} />
      ))}
    </div>
  );
};

export default Items;
